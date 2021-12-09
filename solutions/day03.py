from tools.general import load_input

diagnostics = load_input('day03.txt').split('\n')

# Part 1
BITS = 12
zeroes = [0] * BITS
ones   = [0] * BITS

for i in diagnostics:
    for j in range(BITS):
        if i[j] == '1':
            ones[j] += 1
        else: # i[j] == '0'
            zeroes[j] += 1

gamma   = ''.join(['1' if ones[j] > zeroes[j] else '0' for j in range(BITS)])
epsilon = ''.join(['0' if ones[j] > zeroes[j] else '1' for j in range(BITS)])
print(f'Part 1 => {int(epsilon, 2) * int(gamma, 2)}')

# Part 2
def find_rating(diags, out_bits):

    candidates = diags.copy()
    d = 0

    while len(candidates) > 1:

        n0, n1 = 0, 0

        for c in candidates:
            if c[d] == '0':
                n0 += 1
            else:
                n1 += 1

        dval = out_bits[0 if n0 > n1 else 1]
        candidates = [c for c in candidates if c[d] == dval]
        d += 1

    return candidates[0]

ogr = find_rating(diagnostics, ('0', '1'))
csr = find_rating(diagnostics, ('1', '0'))
print(f'Part 2 => {int(ogr, 2) * int(csr, 2)}')