#!/usr/bin/python3

import re
import itertools

def parse_line(state_map, person_set, line):
    m = re.match(r'(?P<name1>\w+) would (?P<action>\w+) (?P<amount>\d+) happiness units by sitting next to (?P<name2>\w+)\.', line)
    if m:
        key = (m.group('name1'), m.group('name2'))
        amount = int(m.group('amount'))
        if (m.group('action') == 'lose'):
            amount = amount * (-1)
        state_map[key] = amount
        person_set.add(m.group('name1'))

def lookup_happyness(happyness_map, person1, person2):
    if (person1, person2) in happyness_map:
        return happyness_map[(person1, person2)]
    else:
#        print('Warning: person tuple not found: ' + person1 + ' - ' + person2)
        return 0


def calc_setting_happyness(happyness_map, setting):
    happyness = 0
    setting_length = len(setting)
    index = 0
    while (index < setting_length):
        person1 = setting[index]
        person2 = setting[(index+1) % setting_length]
        current_happyness1 = lookup_happyness(happyness_map, person1, person2)
        current_happyness2 = lookup_happyness(happyness_map, person2, person1)
        happyness += current_happyness1 + current_happyness2
        index += 1
    return happyness

def calc_overall_happyness(happyness_map, person_set):
    all_settings = itertools.permutations(person_set)
    best_happyness = None
    for setting in all_settings:
        current_happyness = calc_setting_happyness(happyness_map, setting)
        if (not best_happyness) or (current_happyness > best_happyness):
            best_happyness = current_happyness
    return best_happyness

def main():
    f = open('input.txt','r')
    happyness_map = dict()
    person_set = set()
    for line in f:
        parse_line(happyness_map, person_set, line)
#    print(person_set)
#    print(state_map)
    best_happyness1 = calc_overall_happyness(happyness_map, person_set)
    print('Best Happyness: ' + str(best_happyness1))
    person_set.add('me')
    best_happyness2 = calc_overall_happyness(happyness_map, person_set)
    print('New Happyness with you: ' + str(best_happyness2))

main()
