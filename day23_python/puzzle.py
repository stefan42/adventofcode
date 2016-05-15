from enum import Enum
import re
import sys

# hlf r sets register r to half its current value, then continues with the next instruction.
# tpl r sets register r to triple its current value, then continues with the next instruction.
# inc r increments register r, adding 1 to it, then continues with the next instruction.
# jmp offset is a jump; it continues with the instruction offset away relative to itself.
# jie r, offset is like jmp, but only jumps if register r is even ("jump if even").
# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).

class InstructionType(Enum):
    hlf = 1
    tpl = 2
    inc = 3
    jmp = 4
    jie = 5
    jio = 6

class Machine:

    def __init__(self, instructions):
        self.reg_a = 0
        self.reg_b = 0
        self.inst_ptr = 0
        self.inst = instructions

    def next_step(self):
        (instr_type, reg, offset) = self.inst[self.inst_ptr]
        if (instr_type is InstructionType.hlf):
           self.save_reg(reg, self.load_reg(reg) // 2) 
           self.inst_ptr = self.inst_ptr + 1
        elif (instr_type is InstructionType.tpl):
           self.save_reg(reg, self.load_reg(reg) * 3) 
           self.inst_ptr = self.inst_ptr + 1
        elif (instr_type is InstructionType.inc):
           self.save_reg(reg, self.load_reg(reg) + 1) 
           self.inst_ptr = self.inst_ptr + 1
        elif (instr_type is InstructionType.jmp):
           self.inst_ptr = self.inst_ptr + offset
        elif (instr_type is InstructionType.jie):
           if (self.load_reg(reg) % 2 == 0):
               self.inst_ptr = self.inst_ptr + offset
           else:
               self.inst_ptr = self.inst_ptr + 1
        elif (instr_type is InstructionType.jio):
           if (self.load_reg(reg) == 1):
               self.inst_ptr = self.inst_ptr + offset
           else:
               self.inst_ptr = self.inst_ptr + 1
        else:
            print('next_step: unknown op code: ' + instr_type, file=sys.stderr)
            sys.exit(1)

    def load_reg(self, reg_name):
        if (reg_name == 'a'):
            return self.reg_a
        elif (reg_name == 'b'):
            return self.reg_b
        else:
            print('load_reg: unknown register name: ' + reg_name, file=sys.stderr)
            sys.exit(1)

    def save_reg(self, reg_name, value):
        if (reg_name == 'a'):
            self.reg_a = value
        elif (reg_name == 'b'):
            self.reg_b = value
        else:
            print('save_reg: unknown register name: ' + reg_name, file=sys.stderr)
            sys.exit(1)

    def get_result(self):
        return self.reg_b

    def is_finished(self):
        return self.inst_ptr < 0 or self.inst_ptr >= len(self.inst)

    def __str__(self):
        return 'Machine - self.reg_a: ' + str(self.reg_a) + ' - self.reg_b: ' + str(self.reg_b) + ' - self.inst_ptr: ' + str(self.inst_ptr) + ' - self.inst: ' + str(self.inst)

def parse_instruction(line):
    m = re.match(r'^hlf ([ab])$', line)
    if m:
        return (InstructionType.hlf, m.group(1), None)
    m = re.match(r'^tpl ([ab])$', line)
    if m:
        return (InstructionType.tpl, m.group(1), None)
    m = re.match(r'^inc ([ab])$', line)
    if m:
        return (InstructionType.inc, m.group(1), None)
    m = re.match(r'^jmp ([+-]\d+)$', line)
    if m:
        return (InstructionType.jmp, None, int(m.group(1)))
    m = re.match(r'^jie ([ab]), ([+-]\d+)$', line)
    if m:
        return (InstructionType.jie, m.group(1), int(m.group(2)))
    m = re.match(r'^jio ([ab]), ([+-]\d+)$', line)
    if m:
        return (InstructionType.jio, m.group(1), int(m.group(2)))
    print('Unknown instruction: ' + line, file=sys.stderr)
    sys.exit(1)

def load_instructions(filename):
    f = open(filename, 'r')
    instructions = []
    for line in f:
        instructions.append(parse_instruction(line))
    return instructions

def puzzle1(instructions):
    machine = Machine(instructions)
    while (not machine.is_finished()):
        machine.next_step()
    print('Result1: ' + str(machine.get_result()))
    # print(machine)

def puzzle2(instructions):
    machine = Machine(instructions)
    machine.reg_a = 1
    while (not machine.is_finished()):
        machine.next_step()
    print('Result2: ' + str(machine.get_result()))
    # print(machine)

def main():
    instructions = load_instructions('input.txt')
    puzzle1(instructions)
    puzzle2(instructions)

if __name__ == '__main__':
    main()
