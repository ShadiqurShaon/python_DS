class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def retrive(self,root,left,right):
        if left-right>1 or right-left>1:
            return False
        if not root.left and not root.right:
            return
        if root.left:
            left+=1
            self.retrive(root.left,left,right)
        elif root.right:
            right+=1
            self.retrive(root.right,left,right)

        return[left,right]

    def getTreeHeight(self,root):
        if not root:
            return 0
        left = self.getTreeHeight(root.left)
        right = self.getTreeHeight(root.right)

        if abs(left-right)>1:
            return -1
        else:
            return 1+abs(left-right)
       
       
    
    def inorder(self,root,arr):
        if not root:
            return 
        self.inorder(root.left,arr)
        arr.append(root.val)
        self.inorder(root.right,arr)
        return arr

    

root = Node(1)
# root.left = Node(2)
# root.left.left = Node(3)
# root.left.left.left = Node(4)
root.right = Node(2)
root.right.right = Node(3)
# root.right.right = Node(7)
# root.right.right.right = Node(4)
val = root.getTreeHeight(root)
print(val)

# root2 = root.retrive(root,minv,maxv)
# print("-----------")
# root.inorder(root2)