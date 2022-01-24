"""
A Turing machine that can accept multiple transition functions
AWD 2022
"""

RIGHT = 1
LEFT = -1
BLANK = ' '
NULL = 0

# Define the TM's transition function
copy_bits_tf = {
    # From past AQA June 2013 COMP3 Q7
    ('Sb', '0'): ('S0', 'x', RIGHT),
    ('Sb', '1'): ('S1', 'y', RIGHT),
    ('Sb', '#'): ('St', '#', RIGHT),

    ('S0', '0'): ('S0', '0', RIGHT),
    ('S0', '1'): ('S0', '1', RIGHT),
    ('S0', '#'): ('S0', '#', RIGHT),
    ('S0', BLANK): ('Sr', '0', LEFT),

    ('S1', '0'): ('S1', '0', RIGHT),
    ('S1', '1'): ('S1', '1', RIGHT),
    ('S1', '#'): ('S1', '#', RIGHT),
    ('S1', BLANK): ('Sr', '1', LEFT),

    ('Sr', '0'): ('Sr', '0', LEFT),
    ('Sr', '1'): ('Sr', '1', LEFT),
    ('Sr', '#'): ('Sr', '#', LEFT),
    ('Sr', 'x'): ('Sb', '0', RIGHT),
    ('Sr', 'y'): ('Sb', '1', RIGHT),

}

incremenet_tf = {
    # From Heathcote & Heathcote p275, example 2
    ('S0', BLANK): ('S1', BLANK, LEFT),
    ('S0', '0'): ('S0', '0', RIGHT),
    ('S0', '1'): ('S0', '1', RIGHT),

    ('S1', BLANK): ('S2', '1', RIGHT),
    ('S1', '0'): ('S2', '1', LEFT),
    ('S1', '1'): ('S1', '0', LEFT),

    ('S2', BLANK): ('S3', BLANK, LEFT),
    ('S2', '0'): ('S2', '0', RIGHT),
    ('S2', '1'): ('S2', '1', RIGHT),

}

and_tf = {
    ('Ss', '0'): ('S0', '0', RIGHT),
    ('Ss', '1'): ('S1', '1', RIGHT),

    ('S0', '0'): ('S0', '0', RIGHT),
    ('S0', '1'): ('S0', '1', RIGHT),
    ('S0', '#'): ('S0', '#', RIGHT),
    ('S0', BLANK): ('Sf', '0', LEFT),

    ('S1', '0'): ('S0', '0', RIGHT),
    ('S1', '1'): ('S1', '1', RIGHT),
    ('S1', '#'): ('S1', '#', RIGHT),
    ('S1', BLANK): ('Sf', '1', LEFT),

}

class TM:

    def __init__(self, data: str, transition_function: dict, starting_state: str, halting_states: list,
                 head_starting_position: int = 1):

        self.__transition_function = transition_function
        self.__head_position = head_starting_position - 1
        self.__tape = list(data)
        self.__current_state = starting_state
        self.__halting_states = halting_states.copy()

    def move_head(self, direction: int):
        # This procedure simulates the infinite tape, as opposed to a fixed-length list.

        # If moving left, check there is any tape to the left first. If not, add some.
        if direction == LEFT:
            if self.__head_position == 0:
                self.__tape = [BLANK] + self.__tape
        # If moving right, check there is any tape to the right first. If not, add some.
        elif direction == RIGHT:
            if self.__head_position == len(self.__tape) - 1:
                self.__tape.append(BLANK)

        self.__head_position += direction

    def execute(self, stepping_mode = False):

        while self.__current_state not in self.__halting_states:

            if stepping_mode:
                self.display_state()
                input("\nPress Enter to continue...")

            try:
                new_state, output, movement = \
                    self.__transition_function[(self.__current_state, self.__tape[self.__head_position])]

                self.__current_state = new_state
                self.__tape[self.__head_position] = output
                self.move_head(movement)

            except KeyError:
                print(f"Invalid input. No transition rule defined for state {self.__current_state}, "
                      f"input {self.__tape[self.__head_position]}.")
                break

        self.display_state()

    def display_state(self):
        if self.__current_state in self.__halting_states:
            print(f"\nHALTED! Final state: {self.__current_state}")
        else:
            print(f"Current state:\t\t{self.__current_state}")
        self.display_tape()

    def display_tape(self):
        # Render top and bottom (vertical) border
        top_and_bottom_border = "+---" * (len(self.__tape) + 2) + "+"

        # Print top border
        print(top_and_bottom_border)

        # Render tape contents
        print(" ...|", end="")

        for data in self.__tape:
            print(f" {data} |", end="")

        print("...")

        # Print bottom border
        print(top_and_bottom_border)

        # Show r/w head in correct position
        offset = "    " + "    " * (self.__head_position) + "  "
        print(offset + "^")


if __name__ == "__main__":

    # Get parameters from user
    option = ""
    while option not in ['1', '2', '3']:
        option = input("Which program do you wish to process?\n1) Bit copier\n2) Incrementer\n3) Logical AND\n> ")

    if option == "1":
        tf = copy_bits_tf
        start_state = "Sb"
        halt_states = ["St"]

    elif option == "2":
        tf = incremenet_tf
        start_state = "S0"
        halt_states = ["S3"]

    elif option == "3":
        tf = and_tf
        start_state = "Ss"
        halt_states = ["Sf"]

    tape_data = input(
        "Enter the contents of the tape, using a space for a blank cell and # to signify the end of data.\n> ")

    try:
        head_position = int(input("Enter the starting position of the head (default is 1):\n> "))

    except ValueError:
        head_position = 1

    stepping = input("Use stepping mode? [y/N]\n> ").upper() == "Y"

    # Instantiate TM and execute its transition function
    tm = TM(tape_data, tf, start_state, halt_states, head_position)
    tm.execute(stepping_mode=stepping)
