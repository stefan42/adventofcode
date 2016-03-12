#!/usr/bin/python3

import re

PATTERN = re.compile("[a-z ]+(?P<x1>\d+),(?P<y1>\d+) through (?P<x2>\d+),(?P<y2>\d+)")

def turnOffFieldFunc(field, c):
  field[c] = 0

def turnOnFieldFunc(field, c):
  field[c] = 1

def toggleFieldFunc(field, c):
  if c in field:
    if (field[c] is 0):
      field[c] = 1
    else:
      field[c] = 0
  else:
    field[c] = 1

def processTuple(field, tup, func):
  for x in range(tup[0],tup[2]+1):
    for y in range(tup[1],tup[3]+1):
      func(field, (x,y))

def extractCoords(line):
  m = re.match(PATTERN, line)
  if m:
    return (int(m.group('x1')), int(m.group('y1')), int(m.group('x2')), int(m.group('y2')))
  else:
    return None

def processLine(line, field):
  if (line.startswith('toggle')):
    t = extractCoords(line)
    processTuple(field, t, toggleFieldFunc)
  elif (line.startswith('turn on')):
    t = extractCoords(line)
    processTuple(field, t, turnOnFieldFunc)
  elif (line.startswith('turn off')):
    t = extractCoords(line)
    processTuple(field, t, turnOffFieldFunc)
  else:
    print('unknown')

def processFile(filename, field):
  file = open(filename, 'r')
  for line in file:
    processLine(line, field)
  file.close()
  return field

def createField():
  d = {}
#  for x in (0,1000):
#    for y in (0,1000):
#      d[(x,y)] = 0
  return d

def calcLights(field):
  count = 0
  for k, v in field.items():
    count += v
  return count

def main():
  resField = processFile('input.txt', createField())
  print(calcLights(resField))


main()
