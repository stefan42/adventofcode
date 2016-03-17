#!/usr/bin/python3

import re

def code_line_length(line):
  return len(line.strip())

def escaped_line_length(line):
  (s1,_) = re.subn(r"\\\"", "###\"", line.strip())
  (s2,_) = re.subn(r"\\x[0-9a-fA-F][0-9a-fA-F]", "##x##", s1)
  (s3,_) = re.subn(r"\\\\", "####", s2)
  s4 = re.sub(r"^\"", "\"\\\"", s3)
  s5 = re.sub(r"\"$", "\\\"\"", s4)
  print(s5)
  return len(s5)

def main():
  f = open('input.txt','r')
  overall_diff = 0
  for line in f:
    code_length = code_line_length(line)
    escaped_length = escaped_line_length(line)
    print(line + str(code_length) + " - " + str(escaped_length))
    overall_diff += escaped_length - code_length
  print(str(overall_diff))

main()
