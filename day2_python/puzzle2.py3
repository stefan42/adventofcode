#!/usr/bin/python3

import re

def calc_single_sides(package):
  s1 = package[0]
  s2 = package[1]
  s3 = package[2]
  return (s1*s2, s1*s3, s2*s3)

def smallest_side_area(sides):
  s1 = sides[0]
  s2 = sides[1]
  s3 = sides[2]
  if (s1 <= s2 and s1 <= s3):
    return s1
  elif (s2 <= s1 and s2 <= s3):
    return s2
  else:
    return s3

def calc_package_area(sides):
  s1 = sides[0]
  s2 = sides[1]
  s3 = sides[2]
  return 2*s1 + 2*s2 + 2*s3

def calc_package(package):
  sides = calc_single_sides(package)
  return calc_package_area(sides) + smallest_side_area(sides)

def calc_ribbon_bow(package):
  s1 = package[0]
  s2 = package[1]
  s3 = package[2]
  return s1 * s2 * s3

def calc_ribbon_sides(package):
  s1 = package[0]
  s2 = package[1]
  s3 = package[2]
  if (s1 <= s2 and s1 <= s3):
    if (s2 <= s3):
      return 2*s1 + 2*s2
    else:
      return 2*s1 + 2*s3
  elif (s2 <= s1 and s2 <= s3):
    if (s1 <= s3):
      return 2*s2 + 2*s1
    else:
      return 2*s2 + 2*s3
  else:
    if (s1 <= s2):
      return 2*s3 + 2*s1
    else:
      return 2*s3 + 2*s2

def calc_ribbon(package):
  return calc_ribbon_sides(package) + calc_ribbon_bow(package)

def parse_line(line):
  m = re.match(r"(?P<x>\d+)x(?P<y>\d+)x(?P<z>\d+)", line)
  if m:
    return (int(m.group('x')), int(m.group('y')), int(m.group('z')))
  else:
    return (0,0,0)

def main():
  file = open('input.txt', 'r')
  overall_area = 0;
  overall_ribbon = 0;
  for line in file:
    package = parse_line(line)
    overall_area += calc_package(package)
    overall_ribbon += calc_ribbon(package)
  file.close()
  print('Package: ' + str(overall_area))
  print('Ribbon: ' + str(overall_ribbon))

main()

