def get_data():
    with open("input2.txt", "r") as file:
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
    if get_packet_version(packet) == 4:
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
        subpackets = subpackets.replace(packet, '')
    return packets

def get_packet_versions_sum(packet):
    if get_packet_type(packet) == 4:
        return get_packet_version(packet)
    else:
        if get_length_type(packet) == 0:
            total_length = get_total_length(packet)
            return get_packet_version(packet) + sum([get_packet_versions_sum(p) for p in extract_subpackets(packet[23:])])
        else:
            return get_packet_version(packet) + sum([get_packet_versions_sum(p) for p in extract_subpackets(packet[7:])])

            
def quiz1():
    return get_packet_versions_sum(get_data())

if __name__ == '__main__':
    print(quiz1())