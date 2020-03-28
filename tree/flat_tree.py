class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def make(self, root):
        while root:
            if root.left:
                root = self.swap(root)
            root = root.right
        return root
    def swap(self,root):
        temp_right = root.right
        temp_left = root.left
        root.left = None
        root.right = temp_left
        temp_root = root
        while temp_root.right:
            temp_root = temp_root.right
        temp_root.right = temp_right
        return root
root =Node(1)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.right = Node(6)
tree = Tree()
tree.make(root)

