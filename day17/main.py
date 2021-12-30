import numpy as np
from itertools import product
from operator import add

def get_data():
    with open("input.txt", "r") as file:
        return [int(line) for line in file.readlines()]

class TargetZone:
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y


def quiz1():
    data = get_data()

    gravity = lambda y0, t: y0 - (1 * t*(t+1) / 2)
    gravities = []
    for i in range(1000):
        gravities.append(gravity(0, i))
        

    garray = np.array(gravities, dtype="int")
    max_num = 0
    for i in range(abs(min(garray))):
        garray += i
        filtered = np.absolute(garray[(data[2] <= garray) & (garray <= data[3])])
        if filtered.shape[0] > 0:
            max_num = garray[0]

    return max_num
    

def quiz2():
    data = get_data()
    x = 1

    xs = []
    
    start = data[1]
    while start > 0:
        nums = [start]
        for i in range(start-1, 0, -1):
            nums.append(nums[-1]+i)
        if any([data[0] <= num <= data[1] for num in nums]):
            xs.append(start)
        start -= 1
    
    ys = data[3]
    
    gravity = lambda y0, t: y0 - (1 * t*(t+1) / 2)
    gravities = []
    for i in range(1000):
        gravities.append(gravity(0, i))
        
    garray = np.array(gravities, dtype="int")
    ys = []
    for i in range(data[2], 130):
        if i < 0:
            gcopy = garray + i
            for o in range(1, len(gcopy)):
                gcopy[o] += gcopy[o-1]
            filtered = np.absolute(gcopy[(data[2] <= gcopy) & (gcopy <= data[3])])
            if filtered.shape[0] > 0:
                ys.append(i)
        else:
            garray += i
            filtered = np.absolute(garray[(data[2] <= garray) & (garray <= data[3])])
            if filtered.shape[0] > 0:
                ys.append(i)
    

    all_combinations = sorted(list(product(xs, ys)))
    return len([comb for comb in all_combinations if simulate(*comb, *data)])


def simulate(startx, starty, minx, maxx, miny, maxy):
    point = (0, 0)
    x_vel = startx
    y_vel = starty
    while point[0] <= maxx and point[1] >= miny:
        point = tuple(map(add, point, (x_vel, y_vel)))
        if minx <= point[0] <= maxx and miny <= point[1] <= maxy:
            return True
        x_vel = max(x_vel-1, 0)
        y_vel -= 1
    return False

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())