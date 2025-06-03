
class Node:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right=None

def inorder_traversal(root):
    if root is None:
        return
    inorder_traversal(root.left)
    print(root.data,end=" ")
    inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

root = Node(5)
root.left = Node(6)
root.right = Node(12)
root.right.right = Node(3)
root.left.left = Node(10)
root.left.right = Node(33)
root.left.left.left=Node(56)
preorder_traversal(root)
