from tools.arith import product
from tools.general import load_input

def hex_to_bin(hex_str):

    bin_str = ''

    for c in hex_str:
        binc = bin(int(c, 16))[2:]
        for _ in range(4 - len(binc)):
            # Pad with leading zeroes
            bin_str += '0'
        bin_str += binc

    return bin_str

def get_dec_int(num_str, start, digits, base=2):
    return int(num_str[start : start + digits], base)

def parse_literal(bin_str, pos):

    lit_bits = ''

    more_bits = True
    while more_bits:
        lit_bits += bin_str[pos + 1 : pos + 5]
        if bin_str[pos] == '0':
            more_bits = False
        pos += 5

    return (pos, int(lit_bits, 2))

def parse_operator(bin_str, pos):

    sub_packets = []

    if bin_str[pos] == '0':

        # 15 bit cumulative lenth in bits of all sub-packets follows
        bit_len = get_dec_int(bin_str, pos + 1, 15)
        pos += 16

        sub_str = bin_str[pos : pos + bit_len + 1]
        sub_pos = 0

        while sub_pos < bit_len:
            sub_pos, pac = parse_packet(sub_str, sub_pos)
            sub_packets.append(pac)

        pos += bit_len

    else:

        # 11 bit number of sub-packets follows
        pac_len = get_dec_int(bin_str, pos + 1, 11)
        pos += 12

        for _ in range(pac_len):
            pos, pac = parse_packet(bin_str, pos)
            sub_packets.append(pac)

    return (pos, sub_packets)

def parse_packet(bin_str, pos):

    packet = []

    # Version
    packet.append(get_dec_int(bin_str, pos, 3))
    pos += 3

    # Type
    packet.append(get_dec_int(bin_str, pos, 3))
    pos += 3

    if packet[1] == 4:
        # Literal
        pos, lit = parse_literal(bin_str, pos)
        packet.append(lit)
    else:
        # Operator
        pos, sub_packets = parse_operator(bin_str, pos)
        packet.append(sub_packets)

    return (pos, packet)

def parse_transmission(hex_input):
    return parse_packet(hex_to_bin(hex_input), 0)[1]

def sum_versions(packet):

    ver_sum = packet[0]

    if packet[1] != 4:
        # Operator with one or more sub-packets
        ver_sum += sum(sum_versions(sub_pac) for sub_pac in packet[2])

    return ver_sum

OPR_TYPE = {
    0 : sum,
    1 : product,
    2 : min,
    3 : max,
    5 : (lambda pair : 1 if pair[0] > pair[1] else 0),
    6 : (lambda pair : 1 if pair[0] < pair[1] else 0),
    7 : (lambda pair : 1 if pair[0] == pair[1] else 0)
}

def evaluate_expr(packet):

    if packet[1] == 4:
        # Literal value
        return packet[2]

    operator = OPR_TYPE[packet[1]]
    operands = [evaluate_expr(sub_pac) for sub_pac in packet[2]]

    return operator(operands)

parsed = parse_transmission(load_input('day16.txt'))

print(f'Part 1 => {sum_versions(parsed)}')
print(f'Part 2 => {evaluate_expr(parsed)}')