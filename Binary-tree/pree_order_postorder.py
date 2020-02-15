
class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
class Tree:
    def maketree(self,root,pre,inor):
        if not inor:
            return
        temp = pre.pop(0)
        if temp:
            root = Node(temp)
            for ind,val in enumerate(inor):
                if val==temp:
                    index = ind 
            root.left = self.maketree(root.left,pre,inor[:index])
            root.right = self.maketree(root.right,pre,inor[index+1:])

        return root
        

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
dic_in = {}
for index,item in enumerate(inorder):
    dic_in[item]  = index
root = Node(preorder[0])
tree = Tree()
root = tree.maketree(root,preorder,inorder)

print(root)
       
       
    

    
