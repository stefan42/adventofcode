#!/usr/bin/python3

import re

def parse_line(line):
    m = re.match(r'\w+ can fly (?P<speed>\w+) km/s for (?P<time>\w+) seconds, but then must rest for (?P<rest>\w+) seconds\.', line)
    if m:
        return (int(m.group('speed')), int(m.group('time')), int(m.group('rest')))
    else:
        return None

def calc_full_cycles(speed, time, rest, overall_time):
    cycle_time = time + rest
    cycle_distance = time * speed
    full_distance = int(overall_time / cycle_time) * cycle_distance
    remaining_time = overall_time % cycle_time
#    print(str(speed) + ' ' +  str(time) + ' ' + str(rest) + ' ' + str(overall_time))
#    print(str(full_distance))
#    print(str(remaining_time))
    return (full_distance, remaining_time)

def calc_half_cycle_distance(speed, time, remaining_time):
#    print(str(speed) + ' ' +  str(time) + ' ' + str(remaining_time))
    if time <= remaining_time:
#        print('#1#')
        return time * speed
    else:
#        print('#2#')
        return remaining_time * speed

def eval_reindeer(reindeer, overall_time):
    (speed, time, rest) = reindeer
    (full_distance, remaining_time) = calc_full_cycles(speed, time, rest, overall_time)
    return full_distance + calc_half_cycle_distance(speed, time, remaining_time)

def main():
    f = open('input.txt','r')
    values = []
    for line in f:
        value = parse_line(line)
        if value:
            values.append(value)
    max_dist = None
    for reindeer in values:
       dist = eval_reindeer(reindeer, 2503)
       if (not max_dist) or (max_dist < dist):
           max_dist = dist
    print(max_dist)

main()
