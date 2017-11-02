class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None

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
        temp = []
        runner = self.top
        while runner != None:
            temp.append(runner.val)
            runner = runner.next
        print temp
        return self



def Hanoi_move(num,current,target,other):
    if num == 1:
        target.push(current.pop())
    else:
        Hanoi_move(num-1,current,other,target)
        target.push(current.pop())
        Hanoi_move(num-1,other,target,current)
    return


stack1 = Stack ()
stack1.push(8).push(7).push(6).push(5).push(4).push(3).push(2).push(1)
stack2 = Stack ()
stack3 = Stack ()

stack1.display()
stack2.display()
stack3.display()
print 'running game'
Hanoi_move(8,stack1,stack3,stack2)
stack1.display()
stack2.display()
stack3.display()
