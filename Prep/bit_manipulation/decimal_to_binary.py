def btw(n):
    binary = ['.']
    count = 0
    while n != 0:
        if n >= 2 ** -(count+1):
            binary.append('1')
            n -= 2 ** -(count+1)
        else:
            binary.append('0')
        count += 1
        if count == 33:
            return "ERROR"
    return ''.join(binary)


print btw(.75)
