#!/usr/bin/python3

import re

class Ingredient:

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return 'Ingredient ' + self.name + '(' + str(self.capacity) + ',' + str(self.durability) + ',' + str(self.flavor) + ',' + str(self.texture) + ',' + str(self.calories) +')'

    def __add__(self, other):
        if isinstance(other, Ingredient):
            return Ingredient('cookie', self.capacity + other.capacity, self.durability + other.durability, self.flavor + other.flavor, self.texture + other.texture, self.calories + other.calories)
        else:
            raise Exception('illegal argument')

    def __mul__(self, o):
        if isinstance(o, int):
            return Ingredient(self.name, o*self.capacity, o*self.durability, o*self.flavor, o*self.texture, o*self.calories)
        else:
            raise Exception('illegal argument')

    def get_score(self):
        capacity = max(0, self.capacity)
        durability = max(0, self.durability)
        flavor = max(0, self.flavor)
        texture = max(0, self.texture)
        return capacity * durability * flavor * texture
#        calories = max(0, self.calories)

    def is_healthy(self):
        return self.calories == 500
    

def read_ingredient_file(file_name):
    f = open(file_name,'r')
    result = []
    for line in f:
        m = re.match(r'(?P<name>\w+):[ a-z]*([-0-9]+),[ a-z]*([-0-9]+),[ a-z]*([-0-9]+),[ a-z]*([-0-9]+),[ a-z]*([-0-9]+).*', line)
        if m:
            result.append(Ingredient(m.group('name'), int(m.group(2)),int(m.group(3)),int(m.group(4)),int(m.group(5)),int(m.group(6))))
        else:
            print('does not match')
    return result

def is_valid_mixing(c,d,f,t, limit):
    return (c+d+f+t == limit)

def maybe_possible_mixing(c,d,f,t,limit):
    return (c+d+f+t <= limit)

def get_range(limit):
    return range(1,limit+1)

def main():
    ingredients = read_ingredient_file('input.txt')
    i1 = ingredients[0]
    i2 = ingredients[1]
    i3 = ingredients[2]
    i4 = ingredients[3]
    limit = 100
    best_cookie = None
    best_cookie_score = 0
    best_healthy_cookie = None
    best_healthy_cookie_score = 0
    for c1 in get_range(limit):
        for c2 in get_range(limit):
          if maybe_possible_mixing(c1,c2,0,0, limit):
            for c3 in get_range(limit):
              if maybe_possible_mixing(c1,c2,c3,0, limit):
                for c4 in get_range(limit):
                    if is_valid_mixing(c1,c2,c3,c4, limit):
                        cookie = i1 * c1 + i2 * c2 + i3 * c3 + i4 * c4
                        cookie_score = cookie.get_score()
                        if not best_cookie or cookie_score > best_cookie_score:
                            best_cookie = cookie
                            best_cookie_score = cookie_score
                        if cookie.is_healthy() and (not best_healthy_cookie or cookie_score > best_healthy_cookie_score):
                            best_healthy_cookie = cookie
                            best_healthy_cookie_score = cookie_score
                            # print(str(c1)+' '+str(c2)+' '+str(c3)+' '+str(c4))
    print(best_cookie)
    print(best_cookie_score)
    print(best_healthy_cookie)
    print(best_healthy_cookie_score)
                        


main()
