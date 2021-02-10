class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return '%s_%s' % (self.data, self.height)

    def __bool__(self):
        return self.data

    def set_height(self):
        left_height = -1 if self.left is None else self.left.height
        right_height = -1 if self.right is None else self.right.height
        self.height = max(left_height, right_height) + 1
        return right_height - left_height

    # The self Node is the root of the rotation - the parent node of the subtree to rotate;
    # the root's parent points to the pivot after the rotation;
    # returns Pivot which will become the new parent node
    def right_rotate(self):
        pivot = self.left
        self.left = pivot.right
        pivot.right = self
        self.set_height()
        pivot.set_height()
        return pivot

    def left_rotate(self):
        pivot = self.right
        self.right = pivot.left
        pivot.left = self
        self.set_height()
        pivot.set_height()
        return pivot

    def rebalance(self):
        balance_factor = self.set_height()
        if balance_factor < -1:
            if self.left.set_height() > 0:
                self.left = self.left.left_rotate()
            return self.right_rotate()
        elif balance_factor > 1:
            if self.right.set_height() < 0:
                self.right = self.right.right_rotate()
            return self.left_rotate()
        return self

    def insert(self, data, stack):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                # isleft = True
                stack.append((self, True))
                self.left.insert(data, stack)
                stack.pop()
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                stack.append((self, False))
                self.right.insert(data, stack)
                stack.pop()
        # self.set_height() will surely be called
        if len(stack) > 0:
            parent = stack[-1][0]
            isleft = stack[-1][1]
            if isleft:
                parent.left = self.rebalance()
            else:
                parent.right = self.rebalance()

    def traverse(self, tree, level):
        if self.left is not None:
            self.left.traverse(tree, level + 1)
        if level in tree:
            tree[level].append(self)
        else:
            tree[level] = [self]
        if self.right is not None:
            self.right.traverse(tree, level + 1)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __repr__(self):
        return str(self.root)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            stack = []
            self.root.insert(data, stack)
            self.root = self.root.rebalance()

    def traverse(self):
        if self.root is not None:
            tree = {}
            self.root.traverse(tree, 0)
        for key in sorted(tree.keys()):
            print(tree[key])

    def delete(self, data):
        current = self.root
        if current is None:
            return
        stack = []
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
                isleft = True
            else:
                current = current.right
                isleft = False
            stack.append((parent, isleft))

        if current is None:
            return
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif isleft:
                parent.left = None
            else:
                parent.right = None
        # case 2 - a node with one child
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif isleft:
                parent.left = current.left
            else:
                parent.right = current.left
        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif isleft:
                parent.left = current.right
            else:
                parent.right = current.right
        # case 3 - two children
        else:
            successor_stack = []
            successor_parent = current
            successor = current.right
            while successor.left is not None:
                successor_parent = successor
                successor = successor.left
                successor_stack.append((successor_parent, True))
            if successor_parent != current:
                successor_parent.left = successor.right
                successor.right = current.right
            successor.left = current.left
            if current == self.root:
                self.root = successor
            elif isleft:
                parent.left = successor
            else:
                parent.right = successor
            stack.append((successor, False))
            stack.extend(successor_stack)
        for i in range(len(stack) - 1, 0, -1):
            current = stack[i][0]
            parent = stack[i-1][0]
            isleft = stack[i-1][1]
            if isleft:
                parent.left = current.rebalance()
            else:
                parent.right = current.rebalance()
        self.root = self.root.rebalance()

from random import shuffle

def test_binary_tree():
    # data = [8, 3, 1, 6, 4, 7, 10, 14, 13]
    data = [i for i in range(1, 16)]
    shuffle(data)
    print(data)
    bst = BinarySearchTree()
    # for d in sorted(data):
    for d in data:
        bst.insert(d)
    bst.traverse()
    bst.delete(9)
    bst.delete(8)
    bst.traverse()

def main():
    test_binary_tree()

import sys

if __name__ == '__main__':
    sys.exit(main())
