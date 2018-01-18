def permutation(str1, str2):
    if type(str1) != str or type(str2) != str:
        return False

    if len(str1) != len(str2):
        return False

    check = [0]*127
    for char in str1:
        check[ord(char)] += 1
    for char in str2:
        if check[ord(char)] == 0:
            return False
        check[ord(char)] -= 1
    return True

print permutation('hello','hella')

def permutation2(str1, str2):
    if type(str1) != str or type(str2) != str:
        return False

    if len(str1) != len(str2):
        return False

    check = {}
    for char in str1:
        if char in check:
            check[char] += 1
        else:
            check[char] = 1
    for char in str2:
        if not char in check or check[char] == 0:
            return False
        check[char] -= 1
    return True

print permutation2('hello','helao')
