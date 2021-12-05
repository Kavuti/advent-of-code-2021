import numpy as np
import re

def get_data():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        data = []
        for line in lines:
            matches = re.findall("([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)", line)[0]
            data.append([tuple(map(int, matches[:2])), tuple(map(int, matches[2:]))])
        return data

def is_horizontal_or_vertical(line):
    return line[0][0] == line[1][0] or line[0][1] == line[1][1]

def get_different_range(line):
    if line[0][0] == line[1][0]:
        return "V", (line[0][1], line[1][1]), line[1][0]
    return "H", (line[0][0], line[1][0]), line[0][1]

def check_horizontal_vertical(table, line):
    table_range = get_different_range(line)
    r = table_range[1]
    step = 1 if r[1] >= r[0] else -1
    for i in range(r[0], r[1]+step, step):
        if table_range[0] == 'H':
            table[table_range[2], i] += 1 
        else:
            table[i, table_range[2]] += 1

def quiz1():
    data = get_data()
    table = np.zeros((1000, 1000))
    for line in data:
        if is_horizontal_or_vertical(line):
            check_horizontal_vertical(table, line)
    return sum(list(map(lambda x: 1, table[table >= 2])))
        
def quiz2():
    data = get_data()
    table = np.zeros((1000, 1000))
    for line in data:
        if is_horizontal_or_vertical(line):
            check_horizontal_vertical(table, line)
        else:
            step_h = 1 if line[0][0] < line[1][0] else -1
            step_v = 1 if line[0][1] < line[1][1] else -1

            start_h = line[0][0]
            start_v = line[0][1]
            stop_h = line[1][0]+step_h
            stop_v = line[1][1]+step_v
            i, j = start_h, start_v
            while i != stop_h and j != stop_v:
                table[j, i] += 1
                i += step_h
                j += step_v
                
    return sum(list(map(lambda x: 1, table[table >= 2])))

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
    