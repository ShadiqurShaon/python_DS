class Node:
    def __init__(self,data):
        self.data  = data
        self.left = None
        self.right = None

class BST_main:
    def __init__(self):
        self.list_all = []

    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        self.list_all.append(root.data)
        self.inorder(root.right)

    def inorder2(self,root):
        if root is None:
            return 
        self.inorder2(root.left)
        print(root.data)
        self.inorder2(root.right)

    def create_minheap(self,root,data):
        if root is None:
            root = Node(data)
            return root
        
        if root.data>data:
            root.left = self.create_minheap(root.left,data)
        elif root.data<data:
            root.right = self.create_minheap(root.right,data)
        return root

    def min(self):
        root = None
        for item in self.list_all:
            root = self.create_minheap(root,item)
        self.inorder2(root)

root = Node(8)
root.left = Node(4)
root.right = Node(12)
root.right.left = Node(10)
root.right.right = Node(14)
root.left.left = Node(2)
root.left.right = Node(6)

main = BST_main()
main.inorder(root)
main.min()




        
        
