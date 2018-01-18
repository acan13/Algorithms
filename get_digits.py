def get_digits(string):
    # edge cases
    try:
        return int(string)
    except:
        new_string = ''
        for i in range(len(string)):
            if string[i].isdigit():
                new_string +=  string[i]
        return int(new_string)

print get_digits('0s1a3y5w7h9a2t4?6!8?0')
print get_digits('12346821')
