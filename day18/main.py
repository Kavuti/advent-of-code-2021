import os
from pprint import pprint
import itertools


def read_input():
    lines = []
    with open(os.getcwd() + "/input.txt") as f:
        for line in f:
            lines.append(eval(line))
    return lines


def check_and_manipulate(line):
    new_line = line
    for i, elem in enumerate(line):
        if elem[1] >= 4 and line[i + 1][1] >= 4:
            new_line[i] = [0, elem[1] - 1]
            if i > 0:
                new_line[i - 1][0] += elem[0]
            if i < len(line) - 2:
                new_line[i + 2][0] += line[i + 1][0]
            new_line.pop(i + 1)
            return True, new_line

    for i, elem in enumerate(line):
        if elem[0] >= 10:
            new_line[i] = [elem[0] // 2, elem[1] + 1]
            new_line.insert(i + 1, [(elem[0] + 1) // 2, elem[1] + 1])
            return True, new_line

    return False, line


def sum_lines(left, right):
    try:
        result = left + right
        for elem in result:
            elem[1] += 1
        return result
    except TypeError:
        print(left, right)


def magnitude(line):
    max_depth = max([elem[1] for elem in line])
    while max_depth > 0:
        new_line = line
        for i, elem in enumerate(line):
            if elem[1] == max_depth and line[i + 1][1] == max_depth:
                new_line[i] = [3 * elem[0] + 2 * line[i + 1][0], elem[1] - 1]
                new_line.pop(i + 1)
        line = new_line
        max_depth = max([elem[1] for elem in line])
    return 3 * line[0][0] + 2 * line[1][0]


def get_final_line(lines):
    curr_line = lines[0]
    for i in range(1, len(lines)):
        line = sum_lines(curr_line, lines[i])
        repeat = True
        while repeat:
            repeat = False
            repeat, new_line = check_and_manipulate(line)
            line = new_line
        curr_line = line
    return curr_line


def part1():
    lines = []
    inp = read_input()
    for line in inp:
        lines.append(parse_line(line))
    curr_line = get_final_line(lines)
    print(magnitude(curr_line))


def part2():
    inp = read_input()
    max_magnitude = 0
    for raw in itertools.permutations(inp, 2):
        lines = [parse_line(line) for line in raw]
        curr_line = get_final_line(lines)
        curr_magnitude = magnitude(curr_line)
        if curr_magnitude > max_magnitude:
            max_magnitude = curr_magnitude
    print(max_magnitude)


def parse_line(line, depth=0):
    flat = []
    for elem in line:
        if isinstance(elem, list):
            flat += parse_line(elem, depth + 1)
        else:
            flat += [[elem, depth]]
    return flat


if __name__ == "__main__":
    part1()
    part2()
