class LList(object):
    def __init__(self):
        LList.head = None
    def push(self,val):
        runner = self.head
        while runner != None:
            runner = runner.next
        runner = Node(val)
        return self
    def has_loop(self):
        

class Node(object):
    def __init__(self,val):
        self.val = val
        self.next = None
