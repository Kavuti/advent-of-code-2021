import numpy as np
import re
import sys

from numpy.lib.function_base import flip

def get_data():
    with open("input.txt") as file:
        content = file.read()
        points = [m.split(',') for m in re.findall("[0-9]+,[0-9]+", content)]
        folds = [m.split('=') for m in re.findall("[xy]{1}=[0-9]+", content)]
        return points, folds


def quiz1():
    points, folds = get_data()
    array = np.zeros((1311, 1311), dtype="bool")

    for point in points:
        array[int(point[1]), int(point[0])] = True
    
    flipped_half = np.flip(array[:, int(folds[0][1])+1:], 1)
    non_flipped = array[:, :int(folds[0][1])]
    while non_flipped.shape[1] < flipped_half.shape[1]:
        non_flipped = np.hstack([non_flipped, np.zeros((non_flipped.shape[0], 1))])   
    
    summed = flipped_half | non_flipped
    return np.count_nonzero(summed)
    
def quiz2():
    points, folds = get_data()

    xs = [int(point[0]) for point in points]
    ys = [int(point[1]) for point in points]

    maxx = max(xs)
    maxy = max(ys)

    array = np.zeros((895, 1311), dtype="bool")
    for point in points:
        array[int(point[1]), int(point[0])] = True
    
    for fold in folds:
        if fold[0] == 'x':
            flipped_half = np.flip(array[..., int(fold[1])+1:], 1)
            non_flipped = array[..., 0:int(fold[1])]
        
        else:
            flipped_half = np.flip(array[int(fold[1])+1:, ...], 0)
            non_flipped = array[0:int(fold[1]), ...]
    
        array = flipped_half | non_flipped
    result = ""
    for row in array:
        for col in row:
            result += "#" if col else "."
        result += "\n"
    return result

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())

