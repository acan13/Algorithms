class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.prev = None

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
                    node.right.prev = node
                    return self
                else:
                    node = node.right
            else:
                if node.left == None:
                    node.left = Node(val)
                    node.left.prev = node
                    return self
                else:
                    node = node.left

my_bst = BSTree()
my_bst.add(5).add(1).add(3).add(7).add(9).add(3).add(10).add(5).add(6).add(0).add(3).add(2)

def successor(node):
    print 'running successor'
    if node == None:
        return None

    if node.right != None:
        node = node.right
        while node.left != None:
            node = node.left
        return node

    # turns out the following code is duplicated later

    # if node.prev != None and node.prev.left == node:
    #     if node.prev.val == node.val:
    #         return successor(node.prev)
    #     return node.prev

    if node.prev != None:
        original_node = node
        while node.prev != None and node.prev.right == node:
            node = node.prev
        if node.prev != None and node.prev.val == original_node.val:
            return successor(node.prev)
        return node.prev

    return None



print successor(my_bst.root).val
