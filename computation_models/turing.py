"""
Implmenetation of a simple Turing machine
"""

RIGHT = 1
LEFT = -1
BLANK = ''
NULL = 0

# Define the TM's transition function
tf = {
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

class TM:

    # TODO: Find more elegant solution to the fact that the tape is the same length as the data (and not infinite)
    # Exception handling works but a better way would to always append 1 to the tape when we move right
    # So possibly implement a move_tape() function to achieve this?
    # If the head_position is the end of the tape (i.e. at last position) then add one to the tape
    # Could also do when moving left - if head position is 0 then we need to prepend a blank on the start of the tape

    def __init__(self, data: str, transition_function: dict, starting_state: str, halting_states: list):

        self.__transition_function = transition_function
        self.__head_position = 0
        self.__tape = list(data)
        self.__current_state = starting_state
        self.__halting_states = halting_states.copy()

    def execute(self):

        while self.__current_state not in self.__halting_states:

            try:
                new_state, output, movement = self.__transition_function[(self.__current_state, self.__tape[self.__head_position])]

            except IndexError:
                self.__tape.append(BLANK)

            else:
                self.__tape[self.__head_position] = output
                self.__head_position += movement
                self.__current_state = new_state

        self.display_state()

    def display_state(self):
        print(f"Current state: {self.__current_state}")
        print("Contents of tape:")
        print(self.__tape)
        print(f"Head position: {self.__head_position + 1}")


tm = TM("01#", tf, "Sb", ["St"])
tm.execute()