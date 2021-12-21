def get_data():
    with open("/home/christian/Scrivania/advent-of-code-2021/day16/input2.txt", "r") as file:
        stringed = file.read()
        binary = ""
        for char in stringed:
            binary += (bin(int(char, 16))[2:]).zfill(4)
        return binary

def get_packet_type(packet):
    return 'literal' if packet[3:6] == '100' else 'operator'

def get_packet_version(packet):
    return int(packet[0:3], 2)

def get_length_type(packet):
    return int(packet[6])

def get_total_length(packet):
    return int(packet[7:22], 2)

def extract_packet(packet):
    if get_packet_type(packet) == 'literal':
        curr_char = 6
        while packet[curr_char] == '1':
            curr_char += 5
        return packet[:curr_char+5]
    else:
        if get_length_type(packet) == 0:
            return packet[:23+get_total_length(packet)]
        else:
            return packet[:8+(len(packet[7:]) - (len(packet[7:])%11))]

def extract_subpackets(subpackets):
    packets = []
    while len(subpackets) >= 11:
        packet = extract_packet(subpackets)
        packets.append(packet)
        subpackets = subpackets[len(packet):]
    return packets

def get_packet_versions_sum(packet):
    if get_packet_type(packet) == 'literal':
        return get_packet_version(packet)
    else:
        if get_length_type(packet) == 0:
            total_length = get_total_length(packet)
            subpackets = extract_subpackets(packet[22:])
            return get_packet_version(packet) + sum([get_packet_versions_sum(p) for p in subpackets])
        else:
            subpackets = extract_subpackets(packet[7:])
            return get_packet_version(packet) + sum([get_packet_versions_sum(p) for p in subpackets])

            
def test():
    return extract_packet('1101000101001010010001001000000000')

def quiz1():
    print(get_data())
    return get_packet_versions_sum(get_data())

if __name__ == '__main__':
    print(quiz1())
    print(test())