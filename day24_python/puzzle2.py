import sys
import itertools

def load_packages(filename):
    f = open(filename, 'r')
    result = []
    for line in f:
        result.append(int(line))
    return result

def calc_max_group_weight(packages):
    s = 0
    for p in packages:
        s = s + p
    if (not s % 4 == 0):
        print('calc_max_group_weight: sum is not devidable by 3', file=sys.stderr)
        sys.exit(1)
    return s // 4

def calc_first_group(packages, max_weight, length):
    groups = []
    for group in itertools.combinations(packages, length):
        if (calc_group_weight(group) == max_weight):
            groups.append(group)
    return groups

def has_next_groups(packages, first_group, max_weight, counter):
    remaining_packages = list(set(packages) - set(first_group))
    max_length = len(remaining_packages)
    length = len(first_group)
    while (length < max_length):
        for group in itertools.combinations(remaining_packages, length):
            if (calc_group_weight(group) == max_weight):
                if (counter > 0):
                    return has_next_groups(remaining_packages, group, max_weight, counter - 1)
                else:
                    return True
        length = length + 1
    return False
    

def find_first_match(packages):
    max_weight = calc_max_group_weight(packages)
    length = 1
    max_length = len(packages)
    result_group = None
    while (length < max_length):
        first_groups = calc_first_group(packages, max_weight, length)
        if (first_groups):
            sorted_groups = sorted(first_groups, key=calc_quantum_entanglement)
            print(sorted_groups)
            for first_group in sorted_groups:
                if has_next_groups(packages, first_group, max_weight, 1):
                    return first_group
        length = length + 1
    return None

def calc_quantum_entanglement(group):
    qe = 1
    for g in group:
      qe = qe * g
    return qe

def calc_group_weight(group):
    s = 0
    for g in group:
      s = s + g
    return s

def main():
    packages = load_packages('input.txt')
    print(packages)
    max_weight = calc_max_group_weight(packages)
    print(max_weight)
    result_group = find_first_match(packages) 
    print(result_group)
    print(calc_quantum_entanglement(result_group))

if __name__ == '__main__':
    main()
