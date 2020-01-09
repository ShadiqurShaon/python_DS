class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
class Bst:
    def insert(self,root,data):
        if not root:
            return Node(data)
        elif data<=root.data:

            root.left = self.insert(root.left,data)
        else:
            root.right = self.insert(root.right,data)

        root.height = 1+max(self.get_height(root.left),self.get_height(root.right))
        balance = self.get_balance(root)

        if balance>1 and data<root.left.data:
            # left left
            # right rotate
            return self.right_rotate(root)
        if balance>1 and data>root.left.data:
            # left right
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance<-1 and data>root.right.data:
            # right right
            return self.left_rotate(root)
        if balance<-1 and data<root.right.data:
            # right left
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root
    def get_height(self,root):
        if not root:
            return 0
        return root.height

    def get_balance(self,root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)

    def print_tree(self,root):
        if not root:
            return
        print(root.data)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def right_rotate(self,root):
        y = root.left
        temp = y.right
        y.right = root
        root.left = temp

        root.height = 1+max(self.get_height(root.left),self.get_height(root.right))
        y.height = 1+max(self.get_height(y.left),self.get_height(y.right))

        return y
    
    def left_rotate(self,root):
        y = root.right
        temp = y.left
        y.left = root
        root.right = temp
        root.height = 1+max(self.get_height(root.left),self.get_height(root.right))
        y.height =  1+max(self.get_height(y.left),self.get_height(y.right))
        return y
    
    




bst = Bst()
root = None
root = bst.insert(root,10)
root = bst.insert(root,20)
root = bst.insert(root,30)
root = bst.insert(root,40)
root = bst.insert(root,50)
root = bst.insert(root,25)
# root = bst.insert(root,35)

bst.print_tree(root)
        


