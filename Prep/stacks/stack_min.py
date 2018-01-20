class Node():
    def __init__(self, val, minimum):
        self.minimum = minimum
        self.val = val
        self.prev = None

class Stack():
    def __init__(self):
        self.minimum = None
        self.top = None

    def push(self, val):
        temp = self.top
        self.top = Node(val, self.minimum)
        if self.minimum == None or val < self.minimum:
            self.minimum = val
        self.top.prev = temp
        return self

    def pop(self):
        if self.top == None:
            return None
        self.minimum = self.top.minimum
        temp = self.top
        self.top = temp.prev
        return temp

    def display(self):
        runner = self.top
        print '\nMinimum:', self.minimum
        while runner != None:
            print runner.val
            runner = runner.prev
        return self

my_stack = Stack()
print my_stack.push(5).display().push(1).display().push(3).display().push(6).display().push(-1).display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()
