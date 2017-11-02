import llist
from math import floor

class Stack(object):
    def __init__(self):
        Stack.top = None
    def pop(self):
        if self.top == None:
            return None
        temp = self.top
        self.top = self.top.next
        return temp.val
    def push(self,val):
        temp = self.top
        self.top = Node(val)
        self.top.next = temp
        return self
    def display(self):
        runner = self.top
        print '\nStack'
        while runner != None:
            print runner.val
            runner = runner.next
        return self
    def size(self):
        if self.top==None:
            return 0
        runner=self.top
        counter=1
        while runner.next != None:
            counter+=1
            runner=runner.next
        return counter

class Queue(object):
    def __init__(self):
        Queue.head = None
        Queue.back = None
    def Dequeue(self):
        temp = self.head
        if temp==None:
            return None
        try:
            self.head = self.head.next
        except:
            self.head = None
            self.back = None
        return temp.val
    def Enqueue(self, val):
        if self.back != None:
            self.back.next = Node(val)
            self.back = self.back.next
        else:
            self.back = Node(val)

        if self.head == None:
            self.head = self.back
        return self
    def Display(self):
        arr=[]
        runner = self.head
        while runner != None:
            arr.append(runner.val)
            runner=runner.next
        print arr
        return self
    def Contains(self,val):
        if self.head == None:
            return False;
        node = self.head
        end = False
        while not end:
            if node.val == val:
                return True
            if node.next == None:
                end = True
            node = node.next
        return False
    def IsEmpty(self):
        if self.head == self.back and self.head == None:
            return True
        return False
    def Front(self):
        return self.head.val
    def __str__(self):
        temp = []
        node = self.head
        while node != None:
            temp.append(node.val)
            node = node.next
        temp2 = (temp)
        return 'queue(' + str(temp) + ')'
    def Length(self):
        if self.head == None:
            return 0
        counter=0
        runner=self.head
        while runner != None:
            counter+=1
            runner = runner.next
        return counter


class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

def SwitchAllan(S):
    compcounter=0
    N=S.size()

    Q = Queue()
    sizeS=S.size()

    for i in range(0,int(floor(sizeS/2))):
        temp = S.pop()
        Q.Enqueue(S.pop())
        Q.Enqueue(temp)
        compcounter+=2
    if S.size()>0:
        Q.Enqueue(S.pop())
        compcounter+=1

    for i in range(3):
        if i%2==0:
            #print 'entered first or third'
            while Q.Length() > 0:
                S.push(Q.Dequeue())
                compcounter+=1
        #print 'exited first thing to test'

        if i%2==1:
            #print 'entered second'
            while S.size()>0:
                Q.Enqueue(S.pop())
                compcounter+=1
    print 'Moves:',compcounter,'\nN:',N,'\n'
    return S

def SwitchAlyssa(S):
    N=S.size()
    compcounter=0

    Q = Queue()
    while S.size()>1:
        Q.Enqueue(S.pop())
        Q.Enqueue(S.pop())
        compcounter+=2
    while Q.Length()>0:
        for i in range(0,Q.Length()-2):
            Q.Enqueue(Q.Dequeue())
            compcounter+=1
        S.push(Q.Dequeue())
        S.push(Q.Dequeue())
        compcounter+=2
    print 'Moves:',compcounter,'\nN:',N,'\n'
    return S


newS = Stack()
for i in range(1,1001):
    newS.push(i)

print 'created stack'
newS.display()

print 'Using Allan to switch stack'
SwitchAllan(newS)
print 'Allan switched stack'
newS.display()

print 'Using Allan to switch back'
SwitchAllan(newS)

print 'Switched back, using Alyssa to switch again'
SwitchAlyssa(newS)
print 'Alyssa switched stack'
newS.display()


# newQ = Queue()
# newQ.Enqueue(1).Enqueue(2).Enqueue(3).Enqueue(4)
# newQ.Display()
