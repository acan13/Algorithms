from random import randint

def rando():
    ans = []
    for i in range(98):
        ans.append(randint(-999,999))
    return ans

x = rando()
y = x[:]
y.insert(randint(0,97),1)

# print x[98]
# print y


def answer(x,y):
    counter = 0
    if len(x) > len(y):
        a = x
        b = y
    else:
        a = y
        b = x

    for i in range(len(a)):
        #print 'i',i
        counter+=1
        for j in range(len(b)):
            #print 'j',j
            counter+=1
            if a[i] == b[j]:
                del b[j]
                break
        else:
            return [a[i],counter]

def answer2(x,y):
    counter = 0
    if len(x) > len(y):
        a = x
        b = y
    else:
        a = y
        b = x
    for i in range(len(a)):
        counter+=1
        for j in range(len(b)):
            counter+=1
            if a[i] == b[j]:
                break
        else:
            return [a[i],counter]

print answer(x,y)
print answer2(x,y)
