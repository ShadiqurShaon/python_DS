class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class Tree:
    def insert(self,root,key):
        if not root:
            return Node(key)
        if key<root.data:
            root.left = self.insert(root.left,key)
        else:
            root.right = self.insert(root.right,key)

        root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        if balance > 1 and key<root.left.data:
            return self.rightRotate(root)
        elif balance <-1 and key>root.right.data:
            return self.leftRotate(root)
        elif balance > 1 and key>root.left.data:
            root.left =  self.leftRotate(root.left)
            return self.leftRotate(root)
        elif balance < 1 and key<root.right.data:
            root.right =  self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def rightRotate(self,root):
        y = root.left
        tm = y.right
        y.right = root
        root.left = tm
        root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y
    def leftRotate(self,root):
        y = root.right
        tm = y.left
        y.left = root
        root.right = tm
        root.height = 1+max(self.getHeight(root.left),self.getHeight(root.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y



    def getHeight(self,root):
        if not root:
            return 0
        return root.height

    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left)-self.getHeight(root.right)

    def preorder(self,root):
        if not root:
            return root
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

tree  = Tree()
root = None
root = tree.insert(root,10)
root = tree.insert(root,20)
root = tree.insert(root,30)
root = tree.insert(root,40)
root = tree.insert(root,50)
root = tree.insert(root,25)
tree.preorder(root)
