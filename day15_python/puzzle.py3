#!/usr/bin/python3

import re

class Ingredient:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Ingredient - Name: ' + self.name

def read_ingredient_file(file_name):
    f = open(file_name,'r')
    result = []
    for line in f:
        m = re.match(r'(?P<name>\w+):.*', line)
        if m:
            result.append(Ingredient(m.group('name')))
    return result

def main():
    ingredients = read_ingredient_file('input.txt')
    for i in ingredients:
        print(i)

main()
