class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def find(self,root,sum):
        
        if not root:
            return
        if root.left==None and root.right ==None and sum-root.data==0:
            return True
        sum = sum- root.data
        if sum - root.left.data>-1:
            return self.find(root.left,sum)
        elif sum - root.left.data>-1:
            return self.find(root.right,sum)
        

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.right.right.left = TreeNode(5)

tree = Tree()
print(tree.find(root,22))
