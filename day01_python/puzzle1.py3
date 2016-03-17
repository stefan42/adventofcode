#!/usr/bin/python3

def calc_floor(content):
  level = 0
  for c in content:
    if (c == '('):
      level += 1
    if (c == ')'):
      level -= 1
  return level

def calc_basement_position(content):
  level = 0
  position = 1;
  for c in content:
    if (c == '('):
      level += 1
    if (c == ')'):
      level -= 1
    if (level == -1):
      return position
    position += 1
  return -1
    

def main():
  file = open('input.txt', 'r')
  content = file.read()
  floor = calc_floor(content) 
  print('resulting floor: ' + str(floor))
  position = calc_basement_position(content)
  print('basement position: ' + str(position))
  file.close()

main()

