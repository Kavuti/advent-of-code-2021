def get_data():
    with open("C:/Users/c.cavuti/Desktop/advent-of-code-2021/day14/input2.txt", "r") as file:
        lines = [l.strip() for l in file.readlines()]
        com_dict = dict()
        for command in lines[2:]:
            split = command.split(' -> ')
            com_dict[split[0]] = split[1]
        return lines[0], com_dict

def quiz1():
    line, commands = get_data()
    for _ in range(3):
        new_line = ""
        for i in range(len(line)-1):
            part = line[i:i+2]
            new_line += part[0]
            if part in commands:
                new_line += commands[part]
        new_line += line[-1]
        line = new_line
    
    letters = set(line)
    letters_count = dict()

    max_count = 0
    min_count = 10000000000000
    for letter in letters:
        curr_count = line.count(letter)
        max_count = max(max_count, curr_count)
        min_count = min(min_count, curr_count)
    
    return max_count - min_count

def quiz2():
    line, commands = get_data()
    occurrences = commands.copy()
    for k in occurrences.keys():
        occurrences[k] = 0 
    for i in range(len(line)-1):
        occurrences[line[i]+line[i+1]] = 1

    for i in range(3):
        occ_copy = occurrences.copy()
        for k, v in occurrences.items():
            if v > 0:
                occ_copy[k] = 0
                new_first = k[0]+commands[k]
                new_second = commands[k] + k[1]
                occ_copy[new_first] += v
                occ_copy[new_second] += v
            #print(occurrences)
        occurrences = occ_copy


    print(occurrences)

if __name__ == '__main__':
    print(quiz1())
    quiz2()