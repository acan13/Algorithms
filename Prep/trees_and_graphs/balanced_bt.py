class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BSTree():
    def __init__(self):
        self.root = None
    def add(self, val):
        if self.root == None:
            self.root = Node(val)
            return self
        node = self.root
        while node != None:
            if val > node.val:
                if node.right == None:
                    node.right = Node(val)
                    return self
                else:
                    node = node.right
            else:
                if node.left == None:
                    node.left = Node(val)
                    return self
                else:
                    node = node.left

my_bst = BSTree()
my_bst.add(5).add(1).add(3).add(7).add(9).add(3).add(10).add(5).add(6).add(0)

def is_balanced(tree):
    if tree == None:
        return True
    node = tree.root

    def depth(node):
        if node == None:
            return 1
        left = depth(node.left)
        if left == -1:
            return -1
        right = depth(node.right)
        if right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return 1+ left if left > right else 1 + right

    return not depth(node) == -1

print is_balanced(my_bst)
