from functools import lru_cache

def get_numbers():
    with open("input.txt", "r") as file:
        line = file.readlines()[0]
        line = line.split(',')
        return [int(element) for element in line]

def quiz1():
    numbers = get_numbers()
    numbers.sort()
    mid = len(numbers) // 2
    median = (numbers[mid] + numbers[~mid]) / 2

    calc = [abs(n-median) for n in numbers]
    return int(sum(calc))

def best_round(num):
    if num - int(num) >= 0.6:
        return int(num)+1
    return int(num)

@lru_cache(maxsize=None)
def get_difference(num):
    return sum(list(range(0, num+1)))


def quiz2():
    numbers = get_numbers()
    avg = sum(numbers)/len(numbers)
    avg = best_round(avg)
    calc = [get_difference(abs(n-avg)) for n in numbers]
    return int(sum(calc))



if __name__ == '__main__':
    print(quiz1())
    print(quiz2())