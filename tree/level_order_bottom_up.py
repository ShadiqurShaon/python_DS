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
    def levelOrder(self,root):
        queue =[] 
        result = []
        # result.append(root.data)
        queue.append(root)
        while(queue):
            temp = queue.pop(0)
            result.append(temp.data)

            if temp.left:
                queue.append(temp.left)
            
            if temp.right:
                queue.append(temp.right)
        print(result)
    def revarse_level(self,root):
        q1 = []
        q2 = []
        q1.append(root)
        result = []
        while q1:

            temp_re = []
            while q1:
                temp = q1.pop(0)
                temp_re.append(temp.data)
                if temp.left:
                    q2.append(temp.left)
                if temp.right:
                    q2.append(temp.right)
            result.append(temp_re)
            q1 = q2
            q2 = []
        return result[::-1]

                



if __name__ == "__main__":
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    # root.left.left = Node(7)
    root.right.left = Node(15)
    root.right.right = Node(7)

    tree = Tree()
    # tree.print_tree(root)
    print("----------")
    # tree.levelOrder(root)
    print(tree.revarse_level(root))


        
