class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def getverticleorder(self,root,hd,m):
        if not root:
            return
        if hd in m:
            m[hd].append(root.data)
        else:
            m[hd] =[root.data]

        self.getverticleorder(root.left,hd-1,m)
        self.getverticleorder(root.right,hd+1,m)

    def print_tree(self,root):
        m = {}
        hd = 0

        self.getverticleorder(root,hd,m)

        m = dict(sorted(m.items()))
        for item in m.values():
            print(item)
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.right.left.right = Node(8) 
root.right.right.right = Node(9)
new_node = Node(20)
new_node.print_tree(root)


