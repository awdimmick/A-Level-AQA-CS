"""
Implemntation of a Finite State Machine that represents a validation system for a variable identifier in a programming language.
Identifiers in this language must:
- start with a lowercase letter
- be followed by any combination of lowercase letters and numbers
- contain at least one character
"""

class FSM:

    def __init__(self):
        self.__initial_state = self.s0
        self.__state = self.__initial_state
        self.__accepting_states = [self.s1]
    
    def process_input(self, inp):
        
        #reset initial state
        self.__state = self.__initial_state

        # Iterate through each character in the input string, passing it to the current state function
        for i in inp:
            self.__state(i)

        # We've finished processing the input, so time to see if the final state of the FSM is an accepting state
        if self.__state in self.__accepting_states:
            print("Input is a legal sentence")
        else:
            print("Input is not a legal sentence")

    def current_state(self):
        '''Useful for debugging'''
        return self.__state

    # The FSM's transition function is implemented as a series of state functions that change the internal state of the FSM depending on the input processed
    def s0(self, inp):
        if inp.isalpha():
            self.__state = self.s1
        elif inp.isnumeric():
            self.__state = self.s2
        else:
            raise ValueError(f"{inp} not in FSM alphabet!")
    
    def s1(self, inp):
        if inp.isalpha() or inp.isnumeric():
            self.__state = self.s1
        
        else:
            raise ValueError(f"{inp} not in FSM alphabet!")

    def s2(self, inp):
        if inp.isalpha() or inp.isnumeric():
            self.__state = self.s2
        else:
            raise ValueError(f"{inp} not in FSM alphabet!")


f = FSM()

identifier = input("Enter an identifier to validate: ")
f.process_input(identifier)
