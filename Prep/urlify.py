def urlify(string):
    place = 0
    new_string = ''
    for i in range(len(string)):
        if string[i] == ' ':
            new_string += string[place:i] + '%20'
            place = i + 1
    return new_string

print urlify('this is a test string ')

def urlify3(string):
    for i in range(len(string)-1,-1,-1):
        if string[i] == ' ':
            string = string[0:i] + '%20' + string[i+1:]
    return string


print urlify3('  this is my second test ')
