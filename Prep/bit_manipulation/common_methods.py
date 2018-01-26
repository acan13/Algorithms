def get_bit(n, i):
    return (n & ( 1 << i)) != 0

print get_bit(7,0)
print get_bit(7,1)
print get_bit(7,2)
print get_bit(7,3)
print get_bit(7,4)

def set_bit(n, i):
    return n | ( 1 << i )

print '\n'
print set_bit(8,0)
print set_bit(8,1)
print set_bit(8,2)
print set_bit(8,3)
print set_bit(8,4)

def clear_bit(n, i):
    return n & ~(1 << i)

print '\n'
print clear_bit(8,0)
print clear_bit(8,1)
print clear_bit(8,2)
print clear_bit(8,3)
print clear_bit(8,4)

def update_bit(n, i, one = True):
    val = 1 if one else 0
    mask = ~(1 << i)
    return (n & mask) | (val << i)

print '\n'
print update_bit(8,0)
print update_bit(8,1)
print update_bit(8,2)
print update_bit(8,3)
print update_bit(8,4)
print update_bit(8,0,False)
print update_bit(8,1,False)
print update_bit(8,2,False)
print update_bit(8,3,False)
print update_bit(8,4,False)

print bin(1)
