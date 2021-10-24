"""
LMC Instruction Set

ADD - ADD - 1xx
Add the contents of the given mailbox onto the accumulator (calculator).  Note: the contents of the mailbox are not changed, and the actions of the accumulator are not defined for add instructions that cause sums larger than 3 digits.

SUBTRACT - SUB - 2xx
Subtract the contents of the given mailbox from the accumulator (calculator).  Note: the contents of the mailbox are not changed, and the actions of the accumulator are not defined for subtract instructions that cause negative results -- however, a negative flag will be set so that BRP can be used properly (see below).

STORE - STA - 3xx
Store the contents of the accumulator (calculator) to the mailbox of the given address.  Note: the contents of the accumulator are not changed.

LOAD - LDA - 5xx
Load the contents of the given mailbox onto the accumulator (calculator).  Note: the contents of the mailbox are not changed.

BRANCH ALWAYS - BRA - 6xx
Set the contents of the accumulator (calculator) to the given address.  Note: since the program is stored in memory, data and program instructions all have the same address/location format.

BRANCH IF ZERO - BRZ - 7xx
If the contents of the accumulator (calculator) are 000, the PC (program counter) will be set to the given address.  Note: since the program is stored in memory, data and program instructions all have the same address/location format.

BRANCH IF ZERO OR POSITIVE - BRP - 8xx
If the contents of the accumulator (calculator) are 000 or positive (i.e. the negative flag is not set), the PC (program counter) will be set to the given address.  Note: since the program is stored in memory, data and program instructions all have the same address/location format.

INPUT - INP - 901
Copy the value from the "in box" onto the accumulator (calculator).

OUTPUT - OUt - 902
Copy the value from the accumulator (calculator) to the "out box".  Note: the contents of the accumulator are not changed.

END - HLT - 000
Causes the Little Man Computer to stop executing your program.

DATA LOCATION - DAT
When compiled, a program converts each instruction into a three-digit code.  These codes are placed in sequential mailboxes.  Instead of a program component, this instruction will reserve the next mailbox for data storage.

BINARY DATA FORMAT:

8-bytes per instrruciton

Memory addresses can be from 00-99 (0x00 - 0x63; 0 - 01100011)
Opcodes are from 0-9 (each followed by 00-99)

9 99 - 0101 0110 0011 - 12bit instructions = 3 hex digits

"""

class LMCio:

    @staticmethod
    def display(value):
        print(f"902: {value}")

    @staticmethod
    def input():
        return input("901 instruction: Enter value\n> ")


class LMCMemory:

    def __init__(self, size):
        if 1 <= size <= 2 ** 8:
            self.__memory = [0x0] * size
        else:
            raise ValueError("Memory too large. Size must be between 1 and 255 bytes.")

    def display(self, location=None):
        # Type check required so that inspection of location 0x0 doesn't trigger whole memory dump
        if type(location) != type(None):
            contents = self.__memory[location]
            print(f"Location: {location} ({hex(location)}), Contents: {contents} ({hex(contents)})")
        else:
            for i in range(len(self.__memory)):
                contents = self.__memory[i]
                print(f"Location: {i} ({hex(i)}), Contents: {contents} ({hex(contents)})")

    def write(self, data, location):
        self.__memory[location] = data

    def read(self, location):
        return self.__memory[location]


class LMCProcessor:

    # TODO: Add input/output instructions (901, 902)

    def __init__(self, memory: LMCMemory, io: LMCio):

        self.__memory = memory
        self.__io = io
        self.__halted = False

        self.__registers = {
            'accumulator': 0x0,
            'program_counter': 0x0,
            'instruction_register': 0x0,
            'memory_address_register': 0x0,
            'memory_data_register': 0x0,
        }

        self.__instruction_set = {
            0x0: self.__halt,
            0x1: self.__add,
            0x2: self.__sub,
            0x3: self.__store,
            0x5: self.__load,
            0x6: self.__branch_always,
            0x7: self.__branch_if_zero,
            0x8: self.__branch_if_zero_or_positive,
        }

    @property
    def registers(self):
        return self.__registers.copy()

    def fetch_instruction(self):
        self.__registers['memory_address_register'] = self.__registers['program_counter']
        self.__read_memory()
        self.__registers['instruction_register'] = self.__registers['memory_data_register']
        self.__registers['program_counter'] += 1

    def execute_instruction(self):
        # Use bitwise shift to extract opcode (shift 8 = 2 hex digits)
        opcode = self.__registers['instruction_register'] >> 8
        # Use bitwise AND to mask operand from the instruction
        operand = self.__registers['instruction_register'] & 0x0FF

        print(f"Instruction fetched: opcode: {hex(opcode)}, operand: {hex(operand)}") # redundant, can see inst register

        self.__instruction_set[opcode](operand)

    @property
    def halted(self):
        return self.__halted

    def __halt(self, operand):
        # operand is ignored but included in interface for compliance with other instructions
        self.__halted = True

    def __read_memory(self):
        self.__registers['memory_data_register'] = self.__memory.read(self.__registers['memory_address_register'])

    def __write_memory(self):
        self.__memory.write(self.__registers['memory_data_register'], self.__registers['memory_address_register'])

    def __add(self, operand):
        self.__registers['memory_address_register'] = operand
        self.__read_memory()  # Fetches data from memory and saves on memory_data_register
        self.__registers['accumulator'] += self.__registers['memory_data_register']

    def __sub(self, operand):
        self.__registers['memory_address_register'] = operand
        self.__read_memory()
        self.__registers['accumulator'] -= self.__registers['memory_data_register']

    def __store(self, operand):
        # operand is the memory location to store the value into
        self.__registers['memory_address_register'] = operand
        self.__registers['memory_data_register'] = self.__registers['accumulator']
        self.__write_memory()

    def __load(self, operand):
        # operand is the memory location to retrieve value from
        self.__registers['memory_address_register'] = operand
        self.__read_memory()
        self.__registers['accumulator'] = self.__registers['memory_data_register']

    def __branch_if_zero(self, operand):

        if self.__registers['accumulator'] == 0:
            self.__registers['program_counter'] = operand

    def __branch_always(self, operand):

        self.__registers['program_counter'] = operand

    def __branch_if_zero_or_positive(self, operand):

        if self.__registers['accumulator'] >= 0:
            self.__registers['program_counter'] = operand


class LMCEmulatorController:

    # TODO: Add assembler to enable programs to be loaded from LMC ASM (include symbols?)
    # TODO: Add disassembler to show instructions for each binary encoding of instruction
    # TODO: Add ability to load program from binary
    # TODO: Add "verbose" option to operations to print what instruction they are processing

    memory: LMCMemory = LMCMemory(0x64)  # 100 memory locations
    io: LMCio = LMCio()
    processor: LMCProcessor = LMCProcessor(memory, io)

    @staticmethod
    def assemble(in_asm_file, out_bin_file):
        # TODO: Take in asm file and convert to binary, save binary output
        pass

    @staticmethod
    def load_program():
        LMCEmulatorController.memory.write(0x001, 0x10)
        LMCEmulatorController.memory.write(0x110, 0x00)
        LMCEmulatorController.memory.write(0x110, 0x01)
        LMCEmulatorController.memory.write(0x311, 0x02)

    @staticmethod
    def show_memory(location=None):
        LMCEmulatorController.memory.display(location)

    @staticmethod
    def show_processor_state():
        for key, value in LMCEmulatorController.processor.registers.items():
            print(f"{key}: {str(hex(value))}")

    @staticmethod
    def step():

        while not LMCEmulatorController.processor.halted:

            LMCEmulatorController.processor.fetch_instruction()
            LMCEmulatorController.processor.execute_instruction()
            LMCEmulatorController.show_processor_state()
            command = input("Press Enter to continue with next instruction, or enter M(x,y) to inspect memory: ")

            # Show "Help" information
            if len(command) > 0 and command[0].upper() == "H":
                print("Help: Enter m to see memory, enter m(x) to see contents of memory at location x, enter m(x, y) "
                      "to see contents of memory from locations x to y inclusive.")
                command = input("Press Enter to continue with next instruction, or enter M(x,y) to inspect memory: ")

            # Show memory contents - range provided
            if len(command) > 1 and command[1].upper() == "(":
                if "," in command[1:]:
                    memory_range = command[2:-1].split(",")

                    for i in range(len(memory_range)):
                        memory_range[i] = int(memory_range[i])

                    for location in range(memory_range[0], memory_range[1] + 1):
                        LMCEmulatorController.memory.display(location)

                # Show memory contents - single location provided
                else:
                    location = int(command[2:-1])
                    LMCEmulatorController.memory.display(location)

                input("Press Enter to continue with next instruction...")

            # Show memory contents - no range provided, so show all of memory
            if len(command) == 1 and command[0].upper() == "M":
                LMCEmulatorController.memory.display()
                input("Press Enter to continue with next instruction...")

        print("Processor halted / End of program")

    @staticmethod
    def run():

        while not LMCEmulatorController.processor.halted:

            LMCEmulatorController.processor.fetch_instruction()
            LMCEmulatorController.processor.execute_instruction()


if __name__ == "__main__":

    LMCEmulatorController.load_program()
    LMCEmulatorController.step()
