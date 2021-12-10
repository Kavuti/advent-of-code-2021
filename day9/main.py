def get_numbers():
    with open("input.txt", "r") as file:
        return [l.strip() for l in file.readlines()];

def is_minor(numbers, row, column):
    row_start = row-1
    col_start = column-1
    row_end = row+1
    col_end = column+1
    if row == 0:
        row_start = 0
    if column == 0:
        col_start = 0
    if row == len(numbers)-1:
        row_end = len(numbers)-1
    if column == len(numbers[0])-1:
        col_end = len(numbers[0])-1


    for r in range(row_start, row_end+1):
        for c in range(col_start, col_end+1):
            if numbers[row][column] > numbers[r][c]:
                return False
    return True
    
            
def quiz1():
    to_take = []
    numbers = get_numbers()
    for i, number in enumerate(numbers):
        for j, cipher in enumerate(number):
            if is_minor(numbers, i, j):
                to_take.append(int(number[j]))
    
    return sum(to_take)+len(to_take)


def get_basin(numbers, visited, i, j):
    if i < 0 or j < 0 or i > len(numbers)-1 or j > len(numbers[i])-1 or numbers[i][j] == '9':
        return []
    else:
        if not (i, j) in visited:
            #print(numbers[i][j])
            #input()
            basin = [numbers[i][j]]
            visited.append((i, j))
            basin = basin + get_basin(numbers, visited, i-1, j) + get_basin(numbers, visited, i+1, j) + \
                            get_basin(numbers, visited, i, j-1) + get_basin(numbers, visited, i, j+1)
            return basin
    return []

def quiz2():
    to_take = []
    numbers = get_numbers()
    for i, number in enumerate(numbers):
        for j, cipher in enumerate(number):
            if is_minor(numbers, i, j):
               to_take.append((i, j))

    basins = []
    for tt in to_take:
        basins.append(len(get_basin(numbers, [], tt[0], tt[1])))
    basins.sort()
    
    return basins[-1]*basins[-2]*basins[-3]


if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
        