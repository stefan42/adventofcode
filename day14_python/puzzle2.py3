#!/usr/bin/python3

import re

class Reindeer:

    def __init__(self, name, speed, moving_time, resting_time):
        self.name = name
        self.speed = speed
        self.moving_time = moving_time
        self.resting_time = resting_time
        self.is_moving = True
        self.time_frame = moving_time
        self.distance = 0
        self.points = 0

    def do_step(self):
        if self.is_moving:
            self.distance += self.speed
            self.time_frame -= 1
            if (self.time_frame <= 0):
                self.is_moving = False
                self.time_frame = self.resting_time
        else:
            self.time_frame -= 1
            if (self.time_frame <= 0):
                self.is_moving = True
                self.time_frame = self.moving_time

    def get_distance(self):
        return self.distance

    def add_point(self):
        self.points += 1

    def get_points(self):
        return self.points

    def get_name(self):
        return self.name

def parse_line(line):
    m = re.match(r'(?P<name>\w+) can fly (?P<speed>\w+) km/s for (?P<time>\w+) seconds, but then must rest for (?P<rest>\w+) seconds\.', line)
    if m:
        return (m.group('name'), int(m.group('speed')), int(m.group('time')), int(m.group('rest')))
    else:
        return None


def main():
    f = open('input.txt','r')
    reindeers = []
    for line in f:
        value = parse_line(line)
        if value:
            (name, speed, t_move, t_rest) = value
            reindeers.append(Reindeer(name, speed, t_move, t_rest))
    cycle = 2503
    while cycle > 0:
        cycle -= 1
        cycle_winners = []
        for reindeer in reindeers:
            reindeer.do_step()
            if (not cycle_winners):
                cycle_winners = [reindeer]
            elif (cycle_winners[0].get_distance() < reindeer.get_distance()):
                cycle_winners = [reindeer]
            elif (cycle_winners[0].get_distance() == reindeer.get_distance()):
                cycle_winners.append(reindeer)
        for cycle_winner in cycle_winners:
            cycle_winner.add_point()
    print('Distance Winner:')
    dist_winner = None
    for reindeer in reindeers:
        if (not dist_winner) or (dist_winner.get_distance() < reindeer.get_distance()):
            dist_winner = reindeer
    print('Name ' + dist_winner.get_name() + ' - distance: ' + str(dist_winner.get_distance()) + ' - points: ' + str(dist_winner.get_points()))
    print('Points Winner:')
    points_winner = None
    for reindeer in reindeers:
        if (not points_winner) or (points_winner.get_points() < reindeer.get_points()):
            points_winner = reindeer
    print('Name ' + points_winner.get_name() + ' - distance: ' + str(points_winner.get_distance()) + ' - points: ' + str(points_winner.get_points()))
    print('Overall Scores:')
    for reindeer in reindeers:
        print('Name ' + reindeer.get_name() + ' - distance: ' + str(reindeer.get_distance()) + ' - points: ' + str(reindeer.get_points()))

main()
