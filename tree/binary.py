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

        balace = self.getbalance(root)

        if balace>1 and key>root.right.data:
            

        return root
    def getbalance(self,root):
        if not root:
            return 0
        return self.get_height(root.left)-self.get_height(root.right)
    def get_height(self,root):
        if not root:
            return 0
        return root.height



        
    def print_tree(self,root):
        if not root:
            return
        print(root.data)
        self.print_tree(root.left)
        self.print_tree(root.right)

    def rotate(self,root):
        y = root.left
        temp = y.right
        y.right = root
        root.left = temp

        return y



root = None
bst = Bst()
root = bst.insert(root,10)
root = bst.insert(root,20)
root = bst.insert(root,30)
root = bst.insert(root,40)
root = bst.insert(root,50)
root = bst.insert(root,25)
# root = bst.insert(root,35)
# newroot = root.right
# rotate_root = bst.rotate(newroot)
bst.print_tree(root)
        


