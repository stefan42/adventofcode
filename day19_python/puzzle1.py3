#!/usr/bin/python3

import re
import sys

def read_transitions(prefix):
    f = open(prefix + '_trans.txt','r')
    transitions = []
    for line in f:
        m = re.match('(\w+) => (\w+).*', line)
        if m:
            transitions.append((m.group(1), m.group(2)))
        else:
            print('Error: unable to parse transition: \'' + line + '\'', file=sys.stderr)
    return transitions

def read_string(prefix):
    f = open(prefix + '_string.txt','r')
    return f.read()

def apply_transition(line, transition):
    (left_side, right_side) = transition
    pattern = re.compile(left_side)
    results = set()
    for m in pattern.finditer(line):
        prefix = line[0:m.start()]
        suffix = line[m.end():]
        new_line = prefix + right_side + suffix
        results.add(new_line)
    return results

def main():
    transitions = read_transitions('input')
    line = read_string('input')
    result_set = set()
    for transition in transitions:
        result_set.update(apply_transition(line, transition))
    print('Number of distinct results: ' + str(len(result_set)))

main()
