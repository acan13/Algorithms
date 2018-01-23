class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

class Llist():
    def __init__(self):
        self.head = None
    def push(self, val):
        temp = self.head
        self.head = Node(val)
        self.head.next = temp
        return self
    def display(self):
        runner = self.head
        while runner != None:
            print runner.val
            runner = runner.next

class Leaf():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTree():
    def __init__(self):
        self.root = None
    def add(self, val):
        if self.root == None:
            self.root = Leaf(val)
            return self
        node = self.root
        while node != None:
            if val > node.val:
                if node.right == None:
                    node.right = Leaf(val)
                    return self
                else:
                    node = node.right
            else:
                if node.left == None:
                    node.left = Leaf(val)
                    return self
                else:
                    node = node.left

def depth_lists(tree, level = 0, llists = []):
    if tree == None:
        return
    try:
        tree = tree.root
    except:
        pass
    if len(llists) == level:
        llist = Llist()
        llists.append(llist)
    else:
        llist = llists[level]
    llist.push(tree.val)

    depth_lists(tree.left, level+1, llists)
    depth_lists(tree.right, level+1, llists)

    return llists

my_bst = BSTree()
my_bst.add(5).add(1).add(3).add(7).add(9).add(3).add(10).add(5).add(6)

my_lists = depth_lists(my_bst)
print my_lists

for lst in my_lists:
    print 'new list'
    lst.display()
