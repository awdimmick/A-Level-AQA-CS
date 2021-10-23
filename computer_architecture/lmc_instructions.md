LMC Instruction Set

The LMC has nine instructions.  Each instruction has an assembly mnemonic that is equivalent to a three-digit (decimal) instruction.  In this numerical instruction, the first digit usually represents the instruction, and the second and third digits usually represent a mailbox address.
Summary Table

LOAD

mnemonic - LDA 
numerical/machine code - 5
Load the contents of the given mailbox onto the accumulator (calculator).  Note: the contents of the mailbox are not changed.

STORE

mnemonic - STA 
numerical/machine code - 3
Store the contents of the accumulator (calculator) to the mailbox of the given address.  Note: the contents of the accumulator are not changed.

ADD

mnemonic - ADD 
numerical/machine code - 1
Add the contents of the given mailbox onto the accumulator (calculator).  Note: the contents of the mailbox are not changed, and the actions of the accumulator are not defined for add instructions that cause sums larger than 3 digits.

SUBTRACT

mnemonic - SUB 
numerical/machine code - 2
Subtract the contents of the given mailbox from the accumulator (calculator).  Note: the contents of the mailbox are not changed, and the actions of the accumulator are not defined for subtract instructions that cause negative results -- however, a negative flag will be set so that BRP can be used properly (see below).

INPUT

mnemonic - INP 
numerical/machine code - 901
Copy the value from the "in box" onto the accumulator (calculator).

OUTPUT

mnemonic - OUT 
numerical/machine code - 902
Copy the value from the accumulator (calculator) to the "out box".  Note: the contents of the accumulator are not changed.

END

mnemonic - HLT 
numerical/machine code - 000
Causes the Little Man Computer to stop executing your program.

BRANCH IF ZERO

mnemonic - BRZ 
numerical/machine code - 7
If the contents of the accumulator (calculator) are 000, the PC (program counter) will be set to the given address.  Note: since the program is stored in memory, data and program instructions all have the same address/location format.

BRANCH IF ZERO OR POSITIVE

mnemonic - BRP 
numerical/machine code - 8
If the contents of the accumulator (calculator) are 000 or positive (i.e. the negative flag is not set), the PC (program counter) will be set to the given address.  Note: since the program is stored in memory, data and program instructions all have the same address/location format.

BRANCH ALWAYS

mnemonic - BRA 
numerical/machine code - 6
Set the contents of the accumulator (calculator) to the given address.  Note: since the program is stored in memory, data and program instructions all have the same address/location format.

DATA LOCATION

mnemonic - DAT 
numerical/machine code - (the data)
When compiled, a program converts each instruction into a three-digit code.  These codes are placed in sequential mailboxes.  Instead of a program component, this instruction will reserve the next mailbox for data storage. 
  
 