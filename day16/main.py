from operator import add, mul, gt, eq, lt
from functools import reduce

def get_data():
    with open("input.txt", "r") as file:
        stringed = file.read()
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

def elaborate(packet, length):
    operand = {
        0: add,
        1: mul,
        2: min,
        3: max,
        5: gt,
        6: lt,
        7: eq
    }
    ptype = int(packet[3:6], 2)
    length += 6
    value = ''
    if ptype == 4:
        remaining = packet[6:] 
        while True: 
            if remaining[0] == '0': 
                value += remaining[1:5] 
                remaining = remaining[5:] 
                length += 5 
                break 
            value += remaining[1:5] 
            remaining = remaining[5:] 
            length += 5
        value = int(value,2)
    else:
        length_type = int(packet[6])
        remaining = packet[7:]
        length += 1
        if length_type == 0:
            bit_length = int(remaining[:15], 2)
            remaining = remaining[15:]
            length += 15
            sub_packet_length = 0
            values = []
            while sub_packet_length < bit_length:
                remaining, sub_packet_length, value = elaborate(remaining, sub_packet_length)
                values.append(value)
            length += sub_packet_length
        else:
            num_packets = int(remaining[:11], 2)
            remaining = remaining[11:]
            length += 11
            sub_packet_length = 0
            packet_count = 0
            values = []
            while packet_count < num_packets:
                remaining, sub_packet_length, value = elaborate(remaining, sub_packet_length)
                values.append(value)
                packet_count += 1
            length += sub_packet_length
        
        value = reduce(operand[ptype], values)
            
    return remaining, length, value


def quiz2():
    data = get_data()
    return elaborate(data, 0)[2]
                

if __name__ == '__main__':
    print(quiz1())
    print(quiz2())
