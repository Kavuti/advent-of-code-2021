import numpy as np

def get_data():
    with open("input.txt", "r") as file:
        lines = [list(map(int, list(l.strip()))) for l in file.readlines()]
        return np.array(lines)

def flash(grid):
    todo = True
    done = []
    total = 0
    while todo:
        todo = False
        rows, cols = np.where(grid == 0)
        if rows.size > 0 and cols.size > 0:
            for i in range(rows.shape[0]):
                row, col = rows[i], cols[i]
                if not (row, col) in done:
                    total += 1
                    done.append((row, col))
                    rds = 1 if row > 0 else 0
                    rus = 1 if row < len(grid)-1 else 0
                    cds = 1 if col > 0 else 0
                    cus = 1 if col < len(grid[row])-1 else 0
                    for j in range(row-rds, row+rus+1):
                        for k in range(col-cds, col+cus+1):
                            if grid[j, k] != 0:
                                grid[j, k] = (grid[j, k] + 1) % 10
                                todo = todo or grid[j, k] == 0
    return total

def quiz1():
    grid = get_data()
    total = 0
    for _ in range(100):
        grid = (grid + 1)  % 10
        total += flash(grid)

    return total

def quiz2():
    grid = get_data()
    total = 0
    i = 0
    zeros = np.zeros((grid.shape[0], grid.shape[1]))
    while not np.array_equal(grid, zeros):
        grid = (grid + 1)  % 10
        total += flash(grid)
        i += 1

    return i

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())