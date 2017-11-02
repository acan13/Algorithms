string = "--->-><-><-->-"

def answer(string):
    salutes = 0

    for i in range(len(string)):
        if string[i] == ">":
            for j in range(i+1,len(string)):
                if string[j] == "<":
                    salutes+=2
    return salutes

print answer(string)
