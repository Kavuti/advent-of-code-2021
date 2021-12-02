from os import defpath


def get_commands():
    with open("input.txt", "r") as file:
        return [line.split() for line in file.readlines()]
    

def quiz1():
    position = 0
    depth = 0
    lines = get_commands()
    for line in lines:
        if line[0] == 'forward':
            position += int(line[1])
        elif line[0] == 'up':
            depth -= int(line[1])
        elif line[0] == 'down':
            depth += int(line[1])
        else:
            print("ERRORE", line)
    
    return position*depth

def quiz2():
    position = 0
    depth = 0
    aim = 0
    lines = get_commands()
    for line in lines:
        if line[0] == 'forward':
            position += int(line[1])
            depth += aim*int(line[1])
        elif line[0] == 'up':
            aim -= int(line[1])
        elif line[0] == 'down':
            aim += int(line[1])
        else:
            print("ERRORE", line)
    
    return position*depth

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())