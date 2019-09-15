class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def print_tree(self,node):

        if node is None:
            return 

        self.print_tree(node.left)
        print(node.data)
        self.print_tree(node.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(11)
    root.right = Node(9)
    root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(8)

    tree = Tree()
    tree.print_tree(root)

        
