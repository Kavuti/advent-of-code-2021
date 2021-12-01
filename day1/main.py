def get_numbers():
    with open("input.txt", "r") as file:
        return [int(line) for line in file.readlines()]

def quiz1():
    numbers = get_numbers()
    increased = sum([1 if numbers[i] > numbers[i-1] else 0 for i in range(1, len(numbers))])
    return increased

def quiz2():
    numbers = get_numbers()
    sums = [numbers[i]+numbers[i+1]+numbers[i+2] for i in range(len(numbers)-2)]
    increased = sum([1 if sums[i] > sums[i-1] else 0 for i in range(1, len(sums))])
    return increased

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())