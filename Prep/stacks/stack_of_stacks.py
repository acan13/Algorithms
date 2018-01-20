class Node():
	def __init__(self, val):
		self.val = val
		self.prev = None
class Stack():
	def __init__(self):
		self.top = None
		self.size = 0
	def push(self, val):
		temp = self.top
		self.size += 1
		self.top = Node(val)
		self.top.prev = temp
		return self
	def pop(self):
		if self.top == None:
			return None
		temp = self.top
		self.top = temp.prev
		self.size -= 1
		return temp
class SuperStack():
    def __init__(self, size_limit):
        self.top = None
        self.size_limit = size_limit
    def push(self, val):
        if self.top == None or self.top.val.size == self.size_limit:
            temp = self.top
            self.top = Node(Stack())
            self.top.prev = temp
        self.top.val.push(val)
        return self
    def pop(self):
        if self.top == None:
            return None
        temp = self.top.val.pop()
        if self.top.val.size == 0:
            self.top = self.top.prev
        return temp
    def peek(self):
        return self.top.val.top.val


ss = SuperStack(2)
print ss.push(1).peek()
print ss.top.val
print ss.push(2).peek()
print ss.push(3).peek()
print ss.push(4).peek()
print ss.top.val
print ss.push(5).peek()
print ss.top.val
print ss.push(6).peek()
print ss.top.val
print ss.push(7).peek()
ss.pop()
ss.pop()
ss.pop()
print ss.top.val
print ss.peek()
