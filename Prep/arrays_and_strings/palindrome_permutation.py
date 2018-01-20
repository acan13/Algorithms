def palindrome_permutation(string):
    char_count = {}
    odds = 0
    for char in string:
        if char in char_count:
            char_count[char] += 1
            if char_count[char] % 2 == 0:
                odds -= 1
            else:
                odds += 1
        else:
            char_count[char] = 1
            odds += 1
    if odds <= 1:
        return True
    return False

print palindrome_permutation('allan')
