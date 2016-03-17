#!/usr/bin/python3

VOWELS = {'a','e','i','o','u'}

def is_nice_line(line):
  vowel_count = 0
  pair_found = False
  previous_char = None
  for char in line:
    if (char == previous_char):
      pair_found = True
    if char in VOWELS:
      vowel_count += 1
    if ((previous_char == 'a' and char == 'b') or
        (previous_char == 'c' and char == 'd') or
        (previous_char == 'p' and char == 'q') or
        (previous_char == 'x' and char == 'y')):
      return False
    previous_char = char
  return (vowel_count >= 3) and pair_found

def main():
  f = open('input.txt', 'r')
  nice_line_count = 0;
  for line in f:
    if (is_nice_line(line)):
      nice_line_count += 1
  print('nice lines: ' + str(nice_line_count))

main()
