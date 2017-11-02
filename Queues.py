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
