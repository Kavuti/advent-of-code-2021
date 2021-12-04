from functools import reduce
import numpy as np


def get_data():
    with open("input.txt", "r") as file:
        draws = list(map(int, file.readline().replace('\n', '').split(',')))
        boards = reduce(lambda x, y: x+y, file.readlines()).strip().split('\n\n')
        boards = [board.split('\n') for board in boards]
        boards = [[list(map(int, filter(lambda x: x != '', line.split(' ')))) for line in board ]for board in boards]

        return draws, boards

def get_unmarked_in_board(board):
    return sum([sum([num for num in line]) for line in board])

def quiz1(draws, boards):
    # Naive match only on horizontal lines
    for draw in draws:
        for board in boards:
            for line in board:
                if draw in line:
                    line.remove(draw)
                    if len(line) == 0:
                        unmarked = get_unmarked_in_board(board)
                        return unmarked*draw

def check_board_winning(draws, board):
    board_np = np.array(board)
    winner = False
    for i in range(board_np.shape[1]):
        winner = winner or all(num in draws for num in board_np[:, i])
    for i in range(board_np.shape[0]):
        winner = winner or all(num in draws for num in board_np[i, :])
    return winner

def quiz2(draws, boards):
    all_boards = list(range(len(boards)))
    winners = []
    max_i = 0
    for i in range(1, len(draws)+1):
        for bi, board in enumerate(boards):
            if bi in all_boards and check_board_winning(draws[:i], board):
                winners.append((draws[i-1], np.array(board)))
                print("Winning board: ", board, "with draw ", draws[i-1])
                all_boards.remove(bi)
                max_i = i

    arr = np.array(winners[-1][1])
    for i in range(arr.shape[0]):
        for draw in draws[:max_i]:
            arr[arr == draw] = 0

    unmarked = get_unmarked_in_board(arr)
    return unmarked*winners[-1][0]
                

if __name__ == '__main__':
    draws, boards_data = get_data()
    print(quiz1(draws, [b for b in boards_data])) # somehow this function removes data from boards_data :(
    print(quiz2(draws, [b for b in boards_data])) 

    check_board_winning([1, 4], [[1, 2, 3], [4, 5, 6]])