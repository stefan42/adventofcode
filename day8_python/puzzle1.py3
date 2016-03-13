#!/usr/bin/python3

import re

def code_line_length(line):
  return len(line.strip())

def display_line_length(line):
  s1 = re.sub(r"^\"", "", line.strip())
  s2 = re.sub(r"\"$", "", s1)
  (s3,_) = re.subn(r"\\\"", "#", s2)
  (s4,_) = re.subn(r"\\\\", "#", s3)
  (s5,_) = re.subn(r"\\x[0-9a-fA-F][0-9a-fA-F]","#", s4)
#  print(s5)
  return len(s5)

def main():
  f = open('input.txt','r')
  overall_diff = 0
  for line in f:
    code_length = code_line_length(line)
    display_length = display_line_length(line)
    print(line + str(code_length) + " - " + str(display_length))
    overall_diff += code_length - display_length
  print(str(overall_diff))

main()
