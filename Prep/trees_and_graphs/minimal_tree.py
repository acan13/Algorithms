class Node():
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Tree():
    def __init__(self):
        self.root = None
    def push(self, val):
        self.root = Node(val)
        return self

def shortest_tree(lst):
    if len(lst) == 0:
        return Tree()

    root_idx = int(len(lst)/2)
    tree = Tree()
    tree.push(lst[root_idx])
    tree.root.right = shortest_tree(lst[root_idx+1:]).root
    tree.root.left = shortest_tree(lst[:root_idx]).root
    return tree

test = shortest_tree([0,1,2,3,4,5,6,7,8,9])

print test.root.val
print test.root.left.val
print test.root.right.val
print test.root.left.left.val
print test.root.left.right.val
print test.root.right.left.val
print test.root.right.right.val
print test.root.right.left.left.val
print test.root.right.left.right
print test.root.right.right.left
print test.root.right.right.right
