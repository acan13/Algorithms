def fbtw(n):
    n_str = bin(n)
    print n_str
    lsum = 0
    rsum = 0
    longest = 0
    for i in xrange(2, len(n_str)):
        if n_str[i] == '1':
            rsum += 1
        else:
            lsum += 1
            if rsum + lsum > longest:
                longest = rsum + lsum
            lsum = rsum
            rsum = 0
    if n_str[len(n_str)-1] == '1' and rsum + lsum >= longest:
        return rsum + lsum + 1
    return longest

print fbtw(1775)
