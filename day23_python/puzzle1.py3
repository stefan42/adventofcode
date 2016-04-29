#!/usr/bin/python3

import re
import sys

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

class InstructionType(Enum):
#TODO    

class Machine:

    def __init__(self, instuctions):
        self.reg_a = 0
        self.reg_b = 0
        self.inst_ptr = 0
        self.inst = instructions

    def next_step(self):
        pass

    def get_result(self):
        return self.reg_b

    def is_finished(self):
        return self.inst_ptr < 0 or self.inst_pts >= len(self.inst)

def parse_instruction(line):
    # TODO
    m = re.match('')
    if m:
        # TODO
    else:
        print('Unknown instruction: ' + line, file=sys.stderr)
        sys.exit(1)

def load_instructions(filename):
    f = open(filename, 'r')
    for line in f:
        instructions.add(parse_instruction(line))
    return instruction

def main():
    machine = Machine(load_instructions('input.txt')
    while (not machine.is_finished()):
        machine.next_step()
    print('Result: ' + str(machine.get_result()))

main()
