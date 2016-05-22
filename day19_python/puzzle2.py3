#!/usr/bin/python3

import re
import sys

def split_by_atom(line):
    if (line):
        result = '' + line[0]
        index = 1
        while (index < len(line)):
            if (line[index].isalnum()):
                if (not line[index].islower()):
                    result += '-'
                result += line[index]
            index += 1
        result += '-'
        return result
    else:
        return ''

def read_transitions(prefix):
    f = open(prefix + '_trans.txt','r')
    transitions = {}
    for line in f:
        m = re.match('(\w+) => (\w+).*', line)
        if m:
            left_side = m.group(1)
            right_side = m.group(2)
            add_transition_to_map(transitions, left_side, split_by_atom(right_side))
        else:
            print('Error: unable to parse transition: \'' + line + '\'', file=sys.stderr)
    return transitions

def add_transition_to_map(m, left_side, right_side):
    if (not right_side in m):
        m[right_side] = left_side
    else:
        print('duplicate transition: ' + left_side + ' => ' + right_side + '\n' + str(m), file=sys.stderr)
        sys.exit(1)

def read_string(prefix):
    f = open(prefix + '_string.txt','r')
    return split_by_atom(f.read())

def replace_first_closed_rn_pattern(molecule):
    m = re.match(r'.*?([^-]*-Rn-([^Rn]+?)Ar-).*', molecule)
    if m:
        print('match:\n' + m.group(1) + ' - start: ' + str(m.start(1)) + ' - end: ' + str(m.end(1)) + '\n')
        num_of_repls = calc_rn_content_replacements(m.group(2)) + 1
        new_molecule = molecule[:m.start(1)] + '#-' + molecule[m.end(1):]
        return (num_of_repls, new_molecule)
    else:
        print('no match found')
        return (0, molecule)

def calc_rn_content_replacements(content):
    splits = content.split('Y-')
    result = 0
    for s in splits:
        result += calc_simple_pattern_replacements(s)
    return result

def calc_simple_pattern_replacements(content):
    return content.count('-') - 1

def count_replacements(molecule):
    num_of_repls = 0
    has_rn_patterns = True
    while (has_rn_patterns):
        (rn_repls, molecule) = replace_first_closed_rn_pattern(molecule)
        num_of_repls += rn_repls
        has_rn_patterns = rn_repls > 0
        print('Molecule:\n' + molecule + '\n')
        print('num_of_repls: ' + str(num_of_repls) + '\n')
    num_of_repls += calc_simple_pattern_replacements(molecule)
    return num_of_repls

def main():
    transitions = read_transitions('input')
    print('Transitions: ' + str(transitions))
    molecule = read_string('input')
    print('Start Molecule: ' + molecule)
    num_of_repls = count_replacements(molecule)
    print('Result: ' + str(num_of_repls))

main()
