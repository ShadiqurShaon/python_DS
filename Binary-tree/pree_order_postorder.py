
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def maketree(self,preorder,inorder):
        if not inorder:
            return
        temp = preorder.pop(0)
        if temp:
            root = Node(temp)
            for ind,val in enumerate(inorder):
                if val==temp:
                    index = ind
                    break 
            root.left = self.maketree(preorder,inorder[:index])
            root.right = self.maketree(preorder,inorder[index+1:])
        return root
        
    def inorder(self,root):
        if not root:
            return 
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def preorder(self,root):
        if not root:
            return 
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
dic_in = {}
for index,item in enumerate(inorder):
    dic_in[item]  = index
# root = Node(preorder[0])
tree = Tree()
root = tree.maketree(preorder,inorder)
tree.inorder(root)
# root1 = Node(1)
# root1.left = Node(2)
# root1.right = Node(3)
# root1.left.left = Node(4)
# root1.left.right = Node(5)
# root1.right.left = Node(6)
# root1.right.right = Node(7)
# root1.left.left.right = Node(9)
# root1.right.right.right = Node(10)
# tree.inorder(root1)
# print('---')
# tree.preorder(root1)
# print(root1)
       
       
    

    
