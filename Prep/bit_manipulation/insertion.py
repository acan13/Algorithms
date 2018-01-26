def insertion(n, m, i):
    len_n = len(bin(n)) - 2
    len_m = len(bin(m)) - 2
    mask_left = 0
    mask_right = 0
    for x in xrange(len_n - len_m - i):
        mask_left = (mask_left << 1) + 1
    mask_right << len_m + i
    for x in xrange(len_m):
        mask_right = (mask_right << 1) + 1
    mask_right <<= i
    mask_right = ~mask_right
    mask = mask_left | mask_right
    return (n & mask) | (m << i)

print bin(insertion(int('10000000000',2), int('10011',2), 2))

print bin(insertion(int('10110100',2),int('1110',2),1))

def insertion2(n, m, i):
    len_m = len(bin(m)) - 2
    all_1 = ~0
    left = all_1 << (i + len_m)
    right = ~(all_1 << i)
    mask = left | right
    return (n & mask) | (m << i)

print bin(insertion2(int('10000000000',2), int('10011',2), 2))

print bin(insertion2(int('10110100',2),int('1110',2),1))
