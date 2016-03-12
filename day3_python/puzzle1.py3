#!/usr/bin/python3

import hashlib

def solve_puzzle():
  seed = 'yzbqklnj'
  index = 1;
  while True:
    i = bytes(seed + str(index), 'utf-8')
    r = hashlib.md5(i).hexdigest()
    if (r.startswith("000000")):
      return index
    index += 1

r = solve_puzzle()
print(str(r))
