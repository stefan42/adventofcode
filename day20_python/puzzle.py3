#!/usr/bin/python3

import math
import sys

def get_visiting_elfs(number):
    dividers = set()
    limit = math.ceil(math.sqrt(number))
    index = 1
    while index <= limit:
        if number % index == 0:
            dividers.add(index)
            dividers.add(number // index)
        index += 1
    return dividers

def calc_house_sum(elves):
    sum = 0
    for elf in elves:
        sum += 10 * elf
    return sum

def calc_house_number(limit):
    house_number = 1
    while (calc_house_sum(get_visiting_elfs(house_number)) < limit):
        if (house_number % 10000 == 0):
            print(house_number)
        house_number += 1
    return house_number

def main():
    print('house number: ' + str(calc_house_number(34000000)))


main()
