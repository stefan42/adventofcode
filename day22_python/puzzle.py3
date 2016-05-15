#!/usr/bin/python3

from enum import Enum
import itertools
import sys

#    Magic Missile costs 53 mana. It instantly does 4 damage.
#    Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.

#    Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
#    Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
#    Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.

class SpellType(Enum):
    magic_missile = 1
    drain = 2
    shield = 3
    poison = 4
    recharge = 5

class Player:

    def __init__(self, hit_points, mana):
        self.cost = 0
        self.hit_points = hit_points
        self.mana = mana
        self.armor = 0
        self.effects = {}
        self.spells = []

    def is_alive(self):
        return self.hit_points > 0

    def get_next_spells(self):
        possible_spells = set()
        if self.mana >= 53:
            possible_spells.add(SpellType.magic_missile)
        if self.mana >= 73:
            possible_spells.add(SpellType.drain)
        if self.mana >= 113 and not (SpellType.shield in self.effects):
            possible_spells.add(SpellType.shield)
        if self.mana >= 173 and not (SpellType.poison in self.effects):
            possible_spells.add(SpellType.poison)
        if self.mana >= 229 and not (SpellType.recharge in self.effects):
            possible_spells.add(SpellType.recharge)
        return possible_spells

    def cast_spell(self, spell, boss):
        # print('cast: ' + str(spell))
        self.spells.append(spell)
        if spell is SpellType.magic_missile:
            self.cost = self.cost + 53
            self.mana = self.mana - 53
            boss.hit_points = boss.hit_points - 4
        elif spell is SpellType.drain:
            self.cost = self.cost + 73
            self.mana = self.mana - 73
            self.hit_points = self.hit_points + 2
            boss.hit_points = boss.hit_points - 2
        elif spell is SpellType.shield:
            if SpellType.shield in self.effects:
                print('Error: shield spell already cast', file=sys.stderr)
                sys.exit(1)
            self.cost = self.cost + 113
            self.mana = self.mana - 113
            self.armor = 7
            self.effects[SpellType.shield] = 5
        elif spell is SpellType.poison:
            if SpellType.poison in self.effects:
                print('Error: poison spell already cast', file=sys.stderr)
                sys.exit(1)
            self.cost = self.cost + 173
            self.mana = self.mana - 173
            self.effects[SpellType.poison] = 5
        elif spell is SpellType.recharge:
            if SpellType.recharge in self.effects:
                print('Error: recharge spell already cast ', file=sys.stderr)
                sys.exit(1)
            self.cost = self.cost + 229
            self.mana = self.mana - 229
            self.effects[SpellType.recharge] = 4
        else:
            print('Error: unkown spell type cast: ' + str(spell), file=sys.stderr)
            sys.exit(1)
        if (self.mana < 0):
            print('Error: out of mana!!!', file=sys.stderr)
            sys.exit(1)

    def apply_effects(self, level, boss):
        new_effects = {}
        for k, v in self.effects.items():
            if k is SpellType.shield:
                if v > 0:
                    new_effects[SpellType.shield] = v-1
                else:
                    self.armor = 0
            elif k is SpellType.poison:
                boss.hit_points = boss.hit_points - 3
                if v > 0:
#                    print(str(level) + ' apply poison')
                    new_effects[SpellType.poison] = v-1
#                else:
#                    print(str(level) + ' poison gone')
#                    sys.exit(1) 
            elif k is SpellType.recharge:
                self.mana = self.mana + 101
                if v > 0:
                    new_effects[SpellType.recharge] = v-1
            else:
                print('ERROR: wrong spell type in effect list: ' + str(k), file=sys.stderr)
                sys.exit(1)
        self.effects = new_effects

    def clone(self):
        new_human = Player(self.hit_points, self.mana)
        new_human.cost = self.cost
        new_human.armor = self.armor
        new_human.effects = dict(self.effects)
        new_human.spells = self.spells.copy()
        return new_human

    def __str__(self):
        return 'Player Hit Points: ' + str(self.hit_points) + ' - Mana: ' + str(self.mana)

class Boss:
    def __init__(self,hit_points, damage):
        self.hit_points = hit_points
        self.damage = damage

    def is_alive(self):
        return self.hit_points > 0

    def attack(self, player):
        hits = max(self.damage - player.armor, 1)
        player.hit_points = player.hit_points - hits

    def clone(self):
        return Boss(self.hit_points, self.damage)

    def __str__(self):
        return 'Boss Hit Points: ' + str(self.hit_points)

def process_boss_round(level, best_costs, boss, human, spells_to_cast):
    if (best_costs and (human.cost >= best_costs)):
       return None
#    print('Level: ' + str(level) + ' - Boss turn - Human: ' + str(human) + ' - Boss: ' + str(boss))
    # check that player is not dead
    if (not human.is_alive()):
        # print('Level: ' + str(level) + ' - Boss wins')
        return None
    # is boss is already dead, return costs
    if (not boss.is_alive()):
        print('Level: ' + str(level) + ' - Player wins !!! cost: ' + str(human.cost))
        print('Spells: ' + str(human.spells))
        return human.cost
    # apply effects for this round
    human.apply_effects(level, boss)
    # if boss died by effects, return costs
    if (not boss.is_alive()):
        print('Level: ' + str(level) + ' - Player wins !!! cost: ' + str(human.cost))
        print('Spells: ' + str(human.spells))
        return human.cost
    boss.attack(human)
    return process_human_round(level + 1, best_costs, human, boss, spells_to_cast)


def process_human_round(level, best_costs, human, boss, spells_to_cast):
    if (best_costs and (human.cost >= best_costs)):
       return None
#    print('Level: ' + str(level) + ' - Players turn - Human: ' + str(human) + ' - Boss: ' + str(boss))
    # check that player is not dead
    if (not human.is_alive()):
        # print('Level: ' + str(level) + ' - Boss wins')
        return None
    # is boss is already dead, return costs
    if (not boss.is_alive()):
        print('Level: ' + str(level) + ' - Player wins !!! cost: ' + str(human.cost))
        print('Spells: ' + str(human.spells))
        return human.cost
    # apply effects for this round
    human.apply_effects(level,boss)
    # if boss died by effects, return costs
    if (not boss.is_alive()):
        print('Level: ' + str(level) + ' - Player wins !!! cost: ' + str(human.cost))
        print('Spells: ' + str(human.spells))
        return human.cost
    # get all next spells the user could cast
    next_spells = human.get_next_spells()
    # if he could not cast any spell, he has lost
    if (not next_spells):
        return None
#    print(next_spells)
#    if (spells_to_cast):
#        next_spells = []
#        next_spells.append(spells_to_cast[0])
#        spells_to_cast.pop(0)
    minimum_costs = None
    # print('Level: ' + str(level) + ' - next spells: ' + str(next_spells))
    for spell in next_spells:
        # print('cast: ' + str(spell))
        new_boss = boss.clone()
        new_human = human.clone()
        # print('Level: ' + str(level) + ' - cast spell: ' + str(spell))
        new_human.cast_spell(spell,new_boss)
        #print('Human: ' + str(human) + ' - Boss: ' + str(boss))
        costs = process_boss_round(level + 1, best_costs, new_boss, new_human, spells_to_cast)
        if (costs and (not minimum_costs or (minimum_costs > costs))):
            minimum_costs = costs
            best_costs = costs
    return minimum_costs

def main():
    human = Player(50,500)
    boss = Boss(71,10)
    spells_to_cast = None
# [SpellType.poison, SpellType.recharge, SpellType.magic_missile, SpellType.poison, SpellType.recharge, SpellType.shield, SpellType.poison, SpellType.drain, SpellType.magic_missile ]
#    spells_to_cast = [SpellType.poison, SpellType.magic_missile, SpellType.recharge, SpellType.shield, SpellType.poison, SpellType.recharge, SpellType.magic_missile, SpellType.shield, SpellType.poison, SpellType.magic_missile]
    minimum_costs = process_human_round(1, None, human, boss, spells_to_cast)
    print('human wins - cost: ' + str(minimum_costs))

main()

