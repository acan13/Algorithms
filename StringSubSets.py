counter = 0

def SSS(string,temp=[]):
    global counter
    if not string in temp:
        temp.append(string)
        for i in range(len(string)-1,-1,-1):
            counter+=1
            SSS(string[:i]+string[i+1:],temp)
    return sorted(temp,key=len)



print SSS("ABC")
print counter
