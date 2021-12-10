import re

def get_data():
    with open("input.txt", "r") as file:
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

def guess(num, base):
    if len(num) == 6:
        matches_one = all([c in num  for c in base[0]])
        matches_four = all([c in num for c in base[2]])
        if matches_one:
            if matches_four:
                return '9'
            return '0'
        return '6'
    elif len(num) == 5:
        matches_one = all([c in num for c in base[0]])
        how_many_in_four = sum([1 for c in num if c in base[2]])
        if matches_one:
            return '3'
        if how_many_in_four == 3:
            return '5'
        return '2'
    else:
        sorted_bases = [sorted(c) for c in base]
        idx = sorted_bases.index(sorted(num))
        if idx == 0:
            return '1'
        elif idx == 1:
            return '7'
        elif idx == 2:
            return '4'
        return '8'


def quiz2():
    lines = get_data()
    summed = 0
    for line in lines:
        base = sorted([num for num in line[0] if len(num) in [2, 3, 4, 7]], key=len)
        guesses = [guess(num, base) for num in line[1]]
        summed += int(''.join(guesses))
    return summed

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
