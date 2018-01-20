def compress(string):
    if len(string) < 3:
        return string
    prev = ''
    new_string = ''
    for i in xrange(len(string)):
        if string[i] != prev:
            if prev != '':
                new_string += str(count)
            new_string += string[i]
            count = 0
            prev = string[i]
        count += 1
    new_string += str(count)
    if len(new_string) < len(string):
        return new_string
    return string

print compress('abcdefgggggggggggggg')

def compress2(string):
    if len(string) < 3:
        return string
    prev = ''
    to_compress = []
    net_change = 0
    for i in xrange(len(string)):
        if string[i] != prev:
            if prev != '':
                to_compress.append(str(count))
                net_change += count - 2
            to_compress.append(string[i])
            count = 0
            prev = string[i]
        count += 1
    to_compress.append(str(count))
    net_change += count - 2

    if net_change <= 0:
        return string

    return ''.join(to_compress)


print compress2('abcdefg')
