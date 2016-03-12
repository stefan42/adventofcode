#!/usr/bin/python3

def pair_map_valid(pair_map):
  for pair, positions in pair_map.items():
    last_position = None
    number_positions = len(positions)
    if (number_positions > 2) or ((number_positions == 2) and (positions[1] > (positions[0] + 1))):
      return True
  return False

def is_nice_line(line):
  pair_map = {}
  pair_found = False
  p1_char = None
  p2_char = None
  index = 0
  for char in line:
    if (char == p2_char):
      pair_found = True
    if (p1_char):
      pair = p1_char + char
      if (pair in pair_map):
        pair_map[pair].append(index)
      else:
        pair_map[pair] = [index]
    p2_char = p1_char
    p1_char = char
    index += 1
  return pair_map_valid(pair_map) and pair_found

def main():
  f = open('input.txt', 'r')
  nice_line_count = 0;
  for line in f:
    if (is_nice_line(line)):
      nice_line_count += 1
  print('nice lines: ' + str(nice_line_count))


def do_test(line):
  print(line + ": " + str(is_nice_line(line + '\n')))

def test():
  do_test('qjhvhtzxzqqjkmpb')
  do_test('xxyxx')
  do_test('xyxy')
  do_test('aaa')
  do_test('uurcxstgmygtbstg')
  do_test('ieodomkazucvgmuy')

main()
# test()
