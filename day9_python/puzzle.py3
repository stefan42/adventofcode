#!/usr/bin/python3


import re
import itertools

def parse_line(line):
  m = re.match(r"(?P<c1>\w+) to (?P<c2>\w+) = (?P<dist>\d+)\s*", line)
  if m:
    return (m.group('c1'), m.group('c2'), int(m.group('dist')))
  else:
    return None

def add_to_dist_map(dist_map, dist_item):
  (c1, c2, dist) = dist_item
  dist_map[(c1,c2)] = dist
  dist_map[(c2,c1)] = dist
  return dist_map

def add_to_city_set(city_set, dist_item):
  (c1, c2, _) = dist_item
  city_set.add(c1)
  city_set.add(c2)
  return city_set

def calc_distance(dist_map, cities):
  dist = 0
  previous_city = None
  for city in cities:
    if previous_city:
      dist += dist_map[(previous_city, city)]
    previous_city = city
  return dist

def solve_it(dist_map, city_set):
  perms = itertools.permutations(city_set)
  shortest_dist = None
  longest_dist = None
  for p in perms:
    dist = calc_distance(dist_map, p)
    if (not shortest_dist) or (shortest_dist > dist):
        shortest_dist = dist
    if (not longest_dist) or (longest_dist < dist):
        longest_dist = dist
  print(shortest_dist)
  print(longest_dist)
      
      

def main():
  f = open('input.txt','r')
  dist_map = {}
  city_set = set()
  for line in f:
    parsed_line = parse_line(line)
    dist_map = add_to_dist_map(dist_map, parsed_line)
    city_set = add_to_city_set(city_set, parsed_line)
#  print(str(dist_map))
#  print(str(city_set))
  solve_it(dist_map, city_set)

main()
