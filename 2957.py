import sys
sys.setrecursionlimit(10**6)

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.right = left
        self.left = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.C = 0

    def insert(self, x, node):
        if node == None:
            self.root = Node(x)
            return

        self.C += 1
        if x < node.key:
            if node.left == None:
                node.left = Node(x)
            else:
                self.insert(x, node.left)
        else:
            if node.right == None:
                node.right = Node(x)
            else:
                self.insert(x, node.right)

N = int(sys.stdin.readline())

tree = BinarySearchTree()

for _ in range(N):
    tree.insert(int(sys.stdin.readline()), tree.root)
    print(tree.C)