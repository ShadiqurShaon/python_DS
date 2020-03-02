class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findmax(root):
        if not root:
            return 0
        if root.left == None and root.right == None:
            return 1
        left = 1+findmax(root.left)
        right = 1+findmax(root.right)
        return min(left,right)

tree = TreeNode(3)
tree.left = TreeNode(9)
tree.left.left = TreeNode(5)
tree.left.right = TreeNode(4)
tree.left.left.left = TreeNode(6)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)
tree.right.right.right = TreeNode(17)
print(findmax(tree))