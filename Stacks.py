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

newStack = Stack()

newStack.push(1).push(2).push(3).display()
newStack.pop()
newStack.display()

print newStack
