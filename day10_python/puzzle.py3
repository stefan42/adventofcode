#!/usr/bin/python3


def play_look_and_say(line):
  prev_char = None
  counter = 1
  result = ''
  for c in line:
    if prev_char:
      if c == prev_char:
        counter += 1
      else:
        result += str(counter) + prev_char
        counter = 1
    prev_char = c
  result += str(counter) + prev_char
  return result


def main():
  r = '1113222113'
  c = 0
  while c < 40:
    r = play_look_and_say(r)
    print(str(c) + ": " + str(len(r)))
    c += 1
  
main()
