import numpy as np

def get_data():
    with open("input.txt", "r") as file:
        line = list(map(int, file.readlines()[0].split(',')))
        return line

def compute_trivial(generations, fishes):
    copy = fishes.copy()
    for i in range(generations):
        zeros = len(list(filter(lambda x: x == 0, copy)))
        copy = list(map(lambda x: 7 if x == 0 else x, copy))

        step = 1
        copy = list(map(lambda x: x-step, copy))
        i += step-1
        [copy.append(8) for i in range(zeros)]
    return copy

    
def compute_advanced(generations, meta):
    copy = meta.copy()
    zeros = 0
    for i in range(generations):
        meta[8] += zeros
        meta[6] += zeros
        zeros = meta[0]
        meta = meta[1:] + [0]
    meta[8] += zeros
    return meta

def quiz1():
    return len(compute_trivial(80))
        
def quiz2():
    fishes = get_data()
    meta = []
    for i in range(9):
        meta.append(sum(map(lambda x: 1 if x == i else 0, fishes)))

    meta = compute_advanced(257, meta)
    return sum(meta)

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())