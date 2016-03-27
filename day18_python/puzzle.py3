#!/usr/bin/python3

class Field:

    def __init__(self):
        self.field = []
        self.width = None
        self.height = None

    def read_from_file(self, file_name):
        f = open(file_name,'r')
        height = 0
        for line in f:
            if self.width == None:
                self.width = len(line) - 1
            elif self.width != (len(line) - 1):
                raise Exception('invalid file format')
            for c in line:
                if c == '#':
                    self.field.append(1)
                elif c == '.':
                    self.field.append(0)
            height += 1
        self.height = height

    def show_field(self):
        result = ""
        index = 0
        for cell in self.field:
            if (index > 0) and (index % self.width == 0):
                result += '\n'
            if (cell > 0):
                result += '#'
            else:
                result += '.'
            index += 1
        return result

    def _get_neighbors_(self, index):
        result = set()
        left_top = None
        middle_top = index - self.width
        right_top = None
        left = None
        right = None
        left_bottom = None
        middle_bottom = index + self.width
        right_bottom = None
        if (index % self.width != 0):
            left_top = (index - 1) - self.width
            left = index - 1
            left_bottom = (index - 1) + self.width
        if ((index + 1) % self.width != 0):
            right_top = (index + 1) - self.width
            right = index + 1
            right_bottom = (index + 1) + self.width
        if (middle_top < 0):
            left_top = None
            middle_top = None
            right_top = None
        if (middle_bottom >= (self.width * self.height)):
            left_bottom = None
            middle_bottom = None
            right_bottom = None
        result.add(left_top)
        result.add(middle_top)
        result.add(right_top)
        result.add(left)
        result.add(right)
        result.add(left_bottom)
        result.add(middle_bottom)
        result.add(right_bottom)
        if None in result:
            result.remove(None)
        return result

    def _count_neighbor_lights_(self, index):
        nbs = self._get_neighbors_(index)
        count = 0
        for nb_index in nbs:
            if self.field[nb_index] > 0:
                count += 1
        return count

    def do_next_step(self):
        index = 0
        new_field = []
        for cell in self.field:
            neighbor_lights = self._count_neighbor_lights_(index)
            if cell > 0:
                if neighbor_lights == 2 or neighbor_lights == 3:
                    new_field.append(1)
                else:
                    new_field.append(0)
            else:
                if neighbor_lights == 3:
                    new_field.append(1)
                else:
                    new_field.append(0)
            index += 1
        self.field = new_field

    def count_lights(self):
        count = 0
        for cell in self.field:
            if cell > 0:
                count += 1
        return count

    def turn_corner_lights_on(self):
        self.field[0] = 1
        self.field[self.width - 1] = 1
        self.field[self.width * self.height - 1] = 1
        self.field[self.width * (self.height - 1)] = 1
            

def main():
    field1 = Field()
    field1.read_from_file('input.txt')
    field2 = Field()
    field2.read_from_file('input.txt')
    iters = 100
    while iters > 0:
        field2.turn_corner_lights_on()
#        print(field1.show_field())
#        print()
        field1.do_next_step()
        field2.do_next_step()
        iters -= 1
    field2.turn_corner_lights_on()
#    print(field1.show_field())
    print('Field1: Number of lights: ' + str(field1.count_lights()))
    print('Field2: Number of lights: ' + str(field2.count_lights()))

main()
