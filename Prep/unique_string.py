def unique(string):
    if len(string) > 127:
        return False
    unique_dict = {}
    for char in string:
        if char in unique_dict:
            return False
        unique_dict[char] = 1
    return True

print unique('helo')

def unique2(string):
    if len(string) > 255:
        return False
    used = [False]*255
    for char in string:
        if used[ord(char)]:
            return False
        used[ord(char)] = True
    return True

print unique2('hello')
