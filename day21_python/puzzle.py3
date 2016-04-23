#!/usr/bin/python3

import itertools

class Player:

    def __init__(self,hit_points, damage, armor):
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor

    def is_alive(self):
        return self.hit_points > 0

    def attack(self, other):
        hits = max(self.damage - other.armor, 1)
        other.hit_points = other.hit_points - hits

    def __str__(self):
        return 'Hit Points: ' + str(self.hit_points)

def fight(human, boss):
    while (human.is_alive() and boss.is_alive()):
        human.attack(boss)
        #print('Human: ' + str(human) + ' - Boss: ' + str(boss))
        if (boss.is_alive()):
            boss.attack(human)
            #print('Human: ' + str(human) + ' - Boss: ' + str(boss))

class Item:
    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

    def __str__(self):
        return self.name + ': ' + str(self.cost) + ' - ' + str(self.damage) + ' - ' + str(self.armor)
    def __repr__(self):
        return self.name + ': ' + str(self.cost) + ' - ' + str(self.damage) + ' - ' + str(self.armor)

def weapons():
    return [Item('Dagger',8,4,0)
           ,Item('Shortsword',10,5,0)
           ,Item('Warhammer',25,6,0)
           ,Item('Longsword',40,7,0)
           ,Item('Greataxe',74,8,0)]

def armors():
    return [Item('None',0,0,0)
           ,Item('Leather',13,0,1)
           ,Item('Chainmail',31,0,2)
           ,Item('Splintmail',53,0,3)
           ,Item('Bandedmail',75,0,4)
           ,Item('Platemail',102,0,5)]

def rings():
    return [Item('None',0,0,0)
           ,Item('None',0,0,0)
           ,Item('None',0,0,0)
           ,Item('Damage +1',25,1,0)
           ,Item('Damage +2',50,2,0)
           ,Item('Damage +3',100,3,0)
           ,Item('Defense +1',20,0,1)
           ,Item('Defense +2',40,0,2)
           ,Item('Defense +3',80,0,3)]

def inventories():
    weapon_settings = weapons()
    armor_settings = armors()
    ring_settings = []
    for rs in itertools.combinations(rings(),3):
        ring_settings.append([rs[0],rs[1],rs[2]])
    result_list = []
    for settings in itertools.product(weapon_settings, armor_settings, ring_settings):
        cost = settings[0].cost + settings[1].cost
        damage = settings[0].damage + settings[1].damage
        armor = settings[0].armor + settings[1].armor
        for ring_value in settings[2]:
            cost = cost + ring_value.cost
            damage = damage + ring_value.damage
            armor = armor + ring_value.armor
        result_list.append(Item('Inventory', cost, damage, armor))
    return result_list

def main():
    inventories_asc = sorted(inventories(), key=lambda item: item.cost)
    for inventory in inventories_asc:
        human = Player(100,inventory.damage,inventory.armor)
        boss = Player(109,8,2)
        fight(human, boss)
        if (human.is_alive()):
            print('human wins - cost: ' + str(inventory.cost))
            break
    inventories_desc = sorted(inventories(), key=lambda item: item.cost, reverse=True)
    for inventory in inventories_desc:
        human = Player(100,inventory.damage,inventory.armor)
        boss = Player(109,8,2)
        fight(human, boss)
        if (not human.is_alive()):
            print('boss wins - cost: ' + str(inventory.cost))
            break

main()

