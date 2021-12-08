import re
from itertools import permutations

all_perms = list(map(lambda x: ''.join(x), permutations(['a', 'b', 'c', 'd', 'e', 'f', 'g'])))

def get_data():
    with open("input2.txt", "r") as file:
        lines = file.readlines()
        lines = [line.split(' | ') for line in lines]
        lines = [[line[0].strip().split(' '), line[1].strip().split(' ')] for line in lines]
        return lines

def quiz1():
    lines = get_data()
    counter = 0
    for line in lines:
        for num in line[1]:
            if len(num) in [2, 3, 4, 7]:
                counter += 1

    return counter

def get_from_line(line, *nums):
    result = ''
    for num in nums:
        result += line[num]
    return ''.join(sorted(result))

def get_dicts():
    super_dict = dict()
    for perm in all_perms:
        dictionary = dict()
        dictionary[get_from_line(perm, 0, 1, 2, 4, 5, 6)] = '0'
        dictionary[get_from_line(perm, 2, 5)] = '1'
        dictionary[get_from_line(perm, 0, 2, 3, 4, 6)] = '2'
        dictionary[get_from_line(perm, 0, 2, 3, 5, 6)] = '3'
        dictionary[get_from_line(perm, 1, 2, 3, 5)] = '4'
        dictionary[get_from_line(perm, 0, 1, 3, 5, 6)] = '5'
        dictionary[get_from_line(perm, 0, 1, 3, 4, 5, 6)] = '6'
        dictionary[get_from_line(perm, 0, 2, 5)] = '7'
        dictionary[''.join(sorted(perm))] = '8'
        dictionary[get_from_line(perm, 0, 1, 2, 3, 5, 6)] = '9'
        super_dict[perm] = dictionary
    return super_dict

def quiz2():
    lines = get_data()
    super_dict = get_dicts()
    total = 0
    for line in lines:
        eight = [num for num in line[0] if len(num) == 7][0]
        print(eight)
        perm_dict = super_dict[eight]
        print(perm_dict)
        print(line[1])
        number = int(''.join([perm_dict[''.join(sorted(num))] for num in line[1]]))
        total += number

    return total

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
    # print(all_perms)