def get_data():
    with open("input2.txt", "r") as file:
        stringed = file.read()
        return bin(int(stringed, 16))[2:]

def get_packet_type(packet):
    return 'literal' if packet[3:6] == '100' else 'operator'

def get_packet_version(packet):
    return int(packet[0:3], 2)

def get_length_type(packet):
    return int(packet[6])

def get_total_length(packet):
    return int(packet[7:22], 2)

def quiz1():
    return get_total_length('00111000000000000110111101000101001010010001001000000000')

if __name__ == '__main__':
    print(quiz1())