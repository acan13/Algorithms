from math import ceil, floor
from random import randint
print '*'*100
def balance_point(arr,Lsum=0,Rsum=0,start=0,stop=-1,counter=0):
    #print 'entered function'
    if stop==-1:
        for i in range(len(arr)):
            counter+=1
            Rsum+=arr[i]
        stop=len(arr)
        #print Rsum,'Rsum',stop,'stop',start,'start'

    if Rsum>Lsum:
        loopstart=start
        loopend=int(floor((stop-start)/2))+loopstart
        switch=1
    else:
        loopstart=int(floor((stop-start)/2))+start
        loopend=stop
        switch=-1

    # print 'start',start,'stop',stop
    # print 'loopstart',loopstart,'loopend',loopend

    for i in range(loopstart,loopend):
        Lsum+=arr[i]*switch
        Rsum-=arr[i]*switch
        counter+=1
    #print 'lsum',Lsum,'rsum',Rsum

    # print 'lsum',Lsum,'rsum',Rsum,'\n'

    if Lsum == Rsum:
        #print 'exited\nlsum',Lsum,'rsum',Rsum,'start',start,'stop',stop
        print 'Method 1 counter: ',counter
        return True

    if Lsum>Rsum:
        stop -= int(ceil(float(stop-start)/2))
    else:
        start += int(floor(float(stop-start)/2))

    if stop-start == 1:
        #print 'exited\nlsum',Lsum,'rsum',Rsum,'start',start,'stop',stop
        print 'Method 1 counter: ',counter
        return False

    #print 'lsum',Lsum,'rsum',Rsum,'start',start,'stop',stop

    return balance_point(arr, Lsum, Rsum, start, stop, counter)

def balance_point2(arr):
    Lsum = 0
    Rsum = 0
    counter = 0

    for i in range(len(arr)):
        Rsum+=arr[i]
        counter+=1

    for i in range(len(arr)):
        if Lsum == Rsum:
            print 'Method 2 counter: ',counter
            return True
        Lsum+=arr[i]
        Rsum-=arr[i]
        counter+=1

    print 'Method 2 counter: ',counter
    return False

#print balance_point([1,2,3,4,10])
#print balance_point2([1,2,3,4,10])
#print balance_point([1,2,3,4,5,6,7,8,9,9,2,3,4,5,6,7,8,1])
#print balance_point([1,9,7,4,3,1,2,9])
#print balance_point([1,6,4,7,9,0,3,5,2,6,8,4,8,4,8,2,2,4,6,8,9,4,4,6,4,2,5,7,3,3,2,0])
#print balance_point([5,6,2,7,7,4,2,7,4,8,9,9,5,3,5,39])

#print balance_point([9,4,3,4,2,1,6,0,3])
#print balance_point([3,1,2,10,6,0,10])



testarray=[[]]
for i in range(20):
    for j in range(3001):
        testarray[i].append(randint(0,10))
    if balance_point(testarray[i]) != balance_point2(testarray[i]):
        print testarray[i]
        print 'Method 1:',balance_point(testarray[i])
        print 'Method 2:',balance_point2(testarray[i])
        print '\n\n\n'
        break
    testarray.append([])
