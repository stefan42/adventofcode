#!/usr/bin/python3

import re

class AuntRegister:
    def __init__(self):
        self.all_indexes = set()
        self.state = {}

    def add_aunt(self, aunt):
        if aunt:
            (index, attrs) = aunt
            self.all_indexes.add(index)
            for (attr_name, attr_count) in attrs:
                if attr_name in self.state:
                    if attr_count in self.state[attr_name]:
                        self.state[attr_name][attr_count].add(index)
                    else:
                        self.state[attr_name][attr_count] = {index}
                else:
                    self.state[attr_name] = {attr_count: {index}}

    def find_aunt1(self, tape):
        allowed_indexes = self.all_indexes.copy()
        for (attr_name, attr_count) in tape:
            for cnt, ids in self.state[attr_name].items():
                if cnt != attr_count:
                    allowed_indexes -= ids
        return allowed_indexes

    def find_aunt2(self, tape):
        allowed_indexes = self.all_indexes.copy()
        for (attr_name, attr_count) in tape:
            for cnt, ids in self.state[attr_name].items():
                if attr_name == 'cats' or attr_name == 'trees':
                    if attr_count >= cnt:
                        allowed_indexes -= ids
                elif attr_name == 'pomeranians' or attr_name == 'goldfish':
                    if attr_count <= cnt:
                        allowed_indexes -= ids
                elif cnt != attr_count:
                    allowed_indexes -= ids
        return allowed_indexes

def parse_line(line):
    m_index = re.match(r'Sue (?P<index>\d+): .*', line)
    if m_index:
        aunt_index = int(m_index.group('index'))
        ms_attrs = re.findall(r'(\w+): (\d+)', line)
        aunt_attrs = map(lambda tup: (tup[0], int(tup[1])), ms_attrs)
        return (aunt_index, aunt_attrs) 
    else:
        print('no aunt index found!!!')
        return None

def parse_ticker_tape_line(line):
    m = re.match(r'(\w+): (\d+)',line)
    if m:
        return (m.group(1), int(m.group(2)))
    else:
        print('could not parse ticker tape line!!!')
        return None

def load_ticker_tape(tape_file_name):
    f_tape = open(tape_file_name, 'r')
    tape = []
    for line in f_tape:
        entry = parse_ticker_tape_line(line)
        if entry:
            tape.append(entry)
    return tape
    

def main():
    f_aunts = open('input.txt','r')
    register = AuntRegister()
    for line in f_aunts:
        register.add_aunt(parse_line(line))
#    print(register.state)
    tape = load_ticker_tape('tape.txt')
#    print(tape)
    allowed_aunts1 = register.find_aunt1(tape)
    print('result1: ' + str(allowed_aunts1))
    allowed_aunts2 = register.find_aunt2(tape)
    print('result2: ' + str(allowed_aunts2))

main()
