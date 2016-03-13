#!/usr/bin/python3

import re

WORD16 = 65535

class CircuitState:
  def __init__(self):
    self._state = {}
    self._changed = True
  def set_value(self, var_name, value):
    self._state[var_name] = value
    self._changed = True
  def get_value(self, var_name):
    if (var_name in self._state):
      return self._state[var_name]
    else:
      return None
  def has_changed(self):
    return self._changed
  def reset_changed(self):
    self._changed = False
  def print_values(self):
    print(self._state)

class Value:
  def __init__(self, val):
    self._val = val
  def get_value(self, circuit_state):
    return self._val
  def show_value(self):
    return str(self._val)

class Variable:
  def __init__(self, var_name):
    self._var_name = var_name
  def get_value(self, circuit_state):
    return circuit_state.get_value(self._var_name)
  def show_value(self):
    return self._var_name

class UnaryOp:
  def __init__(self, arg, var_name):
    self._arg = arg
    self._var_name = var_name
  def calc_result(self, circuit_state):
    value = self._arg.get_value(circuit_state)
    if (value != None):
      new_value = self.do_op(value)
      circuit_state.set_value(self._var_name, new_value)
      return True
    else:
      return False
  def do_op(self, value):
    raise NotImplementedError()
  def show_op(self):
    raise NotImplementedError()

class IdOp(UnaryOp):
  def do_op(self, value):
    return value & WORD16
  def show_op(self):
     return self._arg.show_value() + ' -> ' + self._var_name

class NotOp(UnaryOp):
  def do_op(self, value):
    return (~value) & WORD16
  def show_op(self):
     return 'NOT ' + self._arg.show_value() + ' -> ' + self._var_name


class BinaryOp:
  def __init__(self, arg1, arg2, var_name):
    self._arg1 = arg1
    self._arg2 = arg2
    self._var_name = var_name
  def calc_result(self, circuit_state):
    value1 = self._arg1.get_value(circuit_state)
    value2 = self._arg2.get_value(circuit_state)
    if (value1 != None and value2 != None):
      new_value = self.do_op(value1, value2)
      circuit_state.set_value(self._var_name, new_value)
      return True
    else:
      return False
  def do_op(self, value1, value2):
    raise NotImplementedError()
  def show_op(self):
    raise NotImplementedError()

class AndOp(BinaryOp):
  def do_op(self, value1, value2):
    return (value1 & value2) & WORD16
  def show_op(self):
     return self._arg1.show_value() + ' AND ' + self._arg2.show_value() + ' -> ' + self._var_name

class OrOp(BinaryOp):
  def do_op(self, value1, value2):
    return (value1 | value2) & WORD16
  def show_op(self):
     return self._arg1.show_value() + ' OR ' + self._arg2.show_value() + ' -> ' + self._var_name

class LShiftOp(BinaryOp):
  def do_op(self, value1, value2):
    return (value1 << value2) & WORD16
  def show_op(self):
     return self._arg1.show_value() + ' LSHIFT ' + self._arg2.show_value() + ' -> ' + self._var_name

class RShiftOp(BinaryOp):
  def do_op(self, value1, value2):
    return (value1 >> value2) & WORD16
  def show_op(self):
     return self._arg1.show_value() + ' RSHIFT ' + self._arg2.show_value() + ' -> ' + self._var_name


def parse_op(op):
  try:
    num = int(op)
    return Value(num)
  except Exception:
    return Variable(op)
    

def parse_operation(line):
  m = re.match(r"(?P<op>\w+) -> (?P<res>[a-z]+)\s*", line)
  if m:
    op = parse_op(m.group('op'))
    res = m.group('res')
    return IdOp(op, res)
  m = re.match(r"NOT (?P<op>\w+) -> (?P<res>[a-z]+)\s*", line)
  if m:
    op = parse_op(m.group('op'))
    res = m.group('res')
    return NotOp(op, res)
  m = re.match(r"(?P<op1>\w+) AND (?P<op2>\w+) -> (?P<res>[a-z]+)\s*", line)
  if m:
    op1 = parse_op(m.group('op1'))
    op2 = parse_op(m.group('op2'))
    res = m.group('res')
    return AndOp(op1, op2, res)
  m = re.match(r"(?P<op1>\w+) OR (?P<op2>\w+) -> (?P<res>[a-z]+)\s*", line)
  if m:
    op1 = parse_op(m.group('op1'))
    op2 = parse_op(m.group('op2'))
    res = m.group('res')
    return OrOp(op1, op2, res)
  m = re.match(r"(?P<op1>\w+) LSHIFT (?P<op2>\w+) -> (?P<res>[a-z]+)\s*", line)
  if m:
    op1 = parse_op(m.group('op1'))
    op2 = parse_op(m.group('op2'))
    res = m.group('res')
    return LShiftOp(op1, op2, res)
  m = re.match(r"(?P<op1>\w+) RSHIFT (?P<op2>\w+) -> (?P<res>[a-z]+)\s*", line)
  if m:
    op1 = parse_op(m.group('op1'))
    op2 = parse_op(m.group('op2'))
    res = m.group('res')
    return RShiftOp(op1, op2, res)
  print('no match: ' + line)
  return None

def main():
  f = open('input.txt','r')
  remaining_operations = []
  for line in f:
    operation = parse_operation(line)
    if operation:
      remaining_operations.append(operation)
  circuit_state = CircuitState()
  while circuit_state.has_changed():
    circuit_state.reset_changed()
    unprocessed_operations = []
    for operation in remaining_operations:
      if not operation.calc_result(circuit_state):
        unprocessed_operations.append(operation)
    remaining_operations = unprocessed_operations
  if (len(remaining_operations) > 0):
    print('WARNING: there are remaining_operations!')
    for operation in remaining_operations:
      print(operation.show_op())
  circuit_state.print_values()
  print('Wire a: ' + str(circuit_state.get_value('a')))

main()
