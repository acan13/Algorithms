class Queue():
    def __init__(self):
        self.front = None
        self.end = None

    def enqueue(self, val):
        if self.front == None:
            self.front = Node(val)
            self.end = self.front
            return self
        self.end.next = Node(val)
        self.end = self.end.next
        return self
    def dequeue(self):
        if self.is_empty():
            return None
        if self.end == self.front:
            self.end == None
        temp = self.front
        self.front = self.front.next
        return temp
    def is_empty(self):
        if self.front == None:
            return True
        return False

class Node():
    def __init__(self, val, adjacent = []):
        self.val = val
        self.next = None
        self.visited = False
        self.adjacent = adjacent

def route(node1, node2):
    queue = Queue()
    queue.enqueue(node1)
    while not queue.is_empty():
        check_node = queue.dequeue().val

        if check_node == node2:
            return True
        check_node.visited = True
        for new_node in check_node.adjacent:
            if not new_node.visited:
                queue.enqueue(new_node)
    return False

node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

node0.adjacent = [node1, node4, node5]
node1.adjacent = [node3, node4]
node2.adjacent = [node1]
node3.adjacent = [node2, node4]


print route(node1, node5)
