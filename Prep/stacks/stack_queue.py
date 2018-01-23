class Node():
	def __init__(self, val):
		self.val = val
		self.prev = None

class Stack():
    def __init__(self):
        self.top = None
    def push(self, val):
        temp = self.top
        self.top = Node(val)
        self.top.prev = temp
        return self
    def pop(self):
        if self.top == None:
            return None
        temp = self.top
        self.top = temp.prev
        return temp
    def display(self):
        runner = self.top
        while runner != None:
            print runner.val
            runner = runner.prev
        return self

class my_queue():
    def __init__(self):
        self.newest = Stack()
        self.oldest = Stack()
    def enqueue(self, val):
        self.newest.push(val)
        return self
    def dequeue(self):
        if self.oldest.top == None:
            if self.newest.top == None:
                return None
            while self.newest.top.prev != None:
                temp = self.oldest.top
                self.oldest.top = self.newest.pop()
                self.oldest.top.prev = temp
            return self.newest.pop().val
        return self.oldest.pop().val

q = my_queue()
print q.enqueue(1).enqueue(2).enqueue(3).enqueue(4).dequeue()
print q.enqueue(5).enqueue(6).enqueue(7).dequeue()
print q.dequeue()
print q.dequeue()
print q.enqueue(8).dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
