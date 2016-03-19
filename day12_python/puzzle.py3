#!/usr/bin/python3

import json

def iterate_json(input_json):
    if isinstance(input_json, dict):
        accu = 0
        for k, v in input_json.items():
            accu += iterate_json(v)
        return accu
    if isinstance(input_json, list):
        accu = 0
        for o in input_json:
            accu += iterate_json(o)
        return accu
    if isinstance(input_json, str):
        return 0
    if isinstance(input_json, int):
        return input_json
    raise Exception('could not handle: ' + str(input_json)) 

def is_red(input_json):
    return isinstance(input_json, str) and (input_json == 'red')

def iterate_json_without_red(input_json):
    if isinstance(input_json, dict):
        accu = 0
        has_red = False
        for k, v in input_json.items():
            accu += iterate_json_without_red(v)
            has_red = has_red or is_red(v)
        if has_red:
            return 0
        else:
            return accu
    if isinstance(input_json, list):
        accu = 0
        for o in input_json:
            accu += iterate_json_without_red(o)
        return accu
    if isinstance(input_json, str):
        return 0
    if isinstance(input_json, int):
        return input_json
    raise Exception('could not handle: ' + str(input_json)) 

def main():
    f = open('input.txt','r')
    input_str = f.read()
    input_json = json.loads(input_str)
    print('normal: ' + str(iterate_json(input_json)))
    print('without_red: ' + str(iterate_json_without_red(input_json)))

main()
