def acronym(string):
    new_string = ''
    locations = [i for i in range(len(string)) if string[i] == ' ']
    if string[0].isalpha():
        new_string += string[0].upper()
    for location in locations:
        if location + 1 != len(string) and string[location+1].isalpha():
            new_string += string[location+1].upper()
    return new_string

print acronym(" I know a song that gets on everybody's nerves")
