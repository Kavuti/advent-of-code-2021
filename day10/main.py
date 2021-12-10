def get_data():
    with open("input2.txt", "r") as file:
        return [l.strip() for l in file.readlines()]

def get_opposite(par):
    if par == '(':
        return ')'
    if par == '[':
        return ']'
    if par == '{':
        return '}'
    return '>'

def is_open(par):
    return par in ['(', '[', '{', '<']

def get_points(par):
    if par == ')':
        return 3
    if par == ']':
        return 57
    if par == '}':
        return 1197
    return 25137

def quiz1():
    lines = get_data()
    total = 0
    for line in lines:
        par_stack = []
        for par in line:
            if is_open(par):
                par_stack.insert(0, get_opposite(par))
            else:
                if par_stack[0] != par:
                    total += get_points(par)
                    break
                else:
                    par_stack.pop(0)
                
    return total

def quiz2():
    lines = get_data()
    stacks = []
    for line in lines:
        par_stack = []
        valid = True
        for par in line:
            if is_open(par):
                par_stack.insert(0, get_opposite(par))
            else:
                if par_stack[0] != par:
                    valid = False
                    break
                else:
                    par_stack.pop(0)
        if valid:
            stacks.append(''.join(par_stack))
        
    return stacks

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())