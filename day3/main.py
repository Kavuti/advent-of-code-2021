from os import O_TEXT


def get_numbers():
    with open("input.txt", "r") as file:
        return file.readlines()

def quiz1():
    numbers = get_numbers()
    gamma = ''
    epsylon = ''
    for i in range(len(numbers[0])-1):
        ciphers = [n[i] for n in numbers]
        zeros = ciphers.count('0')
        ones = ciphers.count('1')
        if zeros > ones:
            gamma += '0'
            epsylon += '1'
        else:
            gamma += '1'
            epsylon += '0'
    gammaint = int(gamma, 2)
    epsylonint = int(epsylon, 2)
    return gammaint*epsylonint

def quiz2():
    numbers = get_numbers()
    oxygen = int(reduce_numbers(numbers, 0, False), 2)
    codue = int(reduce_numbers(numbers, 0, True), 2)
    return oxygen*codue

def reduce_numbers(numbers, position, least):
    if len(numbers) == 1:
        return numbers[0]
    
    ciphers = [n[position] for n in numbers]
    zeros = ciphers.count('0')
    ones = ciphers.count('1')
    to_pick = None
    if zeros > ones:
        to_pick = '1' if least else '0'
    else:
        to_pick = '0' if least else '1'
    
    indexes = [i for i in range(len(ciphers)) if ciphers[i] == to_pick]
    return reduce_numbers([numbers[i] for i in indexes], position+1, least)

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
