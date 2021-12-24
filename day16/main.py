def get_data():
    with open("input.txt", "r") as file:
        stringed = file.readlines()[0].strip()
        binary = ""
        for char in stringed:
            binary += (bin(int(char, 16))[2:]).zfill(4)
        return binary

def quiz1():
    data = get_data()
    i = 0
    total = 0
    while i < len(data) and '1' in data[i:]:
        version = int(data[i:i+3], 2)
        total += version
        ptype = int(data[i+3:i+6], 2)
        i += 6
        if ptype == 4:
            curr_char = i
            while data[curr_char] == '1':
                curr_char += 5
            curr_char += 5
            i = curr_char
        else:
            lt = int(data[i])
            i += 1
            if lt == 0:
                i += 15
            else:
                i += 11
    return total          
    
if __name__ == '__main__':
    print(get_data())
    print(quiz1())
