class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if not root:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)


def insert(root,element):
    if not root:
        return Node(element)
    if element<root.data:
        root.left = insert(root.left,element)
    else:
        root.right = insert(root.right,element)
    return root

arr = [-10,-3,0,5,9]
mroot = len(arr)//2
root = Node(arr[mroot])
for i,v in enumerate(arr):
    if i!= mroot:
        root = insert(root,v)
preorder(root)
