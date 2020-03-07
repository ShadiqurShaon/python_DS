class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def find(self,root,sum,arr,result):
        if not root:
            return 
        if root.left is None and root.right is None and sum-root.data==0:
            arr.append(root.data)
            result.append(arr)
            return result 
        self.find(root.left,sum-root.data,arr+[root.data],result)
        self.find(root.right,sum-root.data,arr+[root.data],result)
        
        return result
        

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(2)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
root.right.right.left = TreeNode(5)

tree = Tree()
print(tree.find(root,22,[],[]))
