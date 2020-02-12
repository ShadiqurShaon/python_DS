class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

    def levelOrder(self,root):
        result = []
        queue = []
        queue.append(root)
        counter = 0
        counter2 = 1
        while queue:
            tempre = []
            while counter2>0:
                nroot = queue.pop(0)
                tempre.append(nroot.val)
                counter2-=1
                if nroot.left:
                    queue.append(nroot.left)
                    counter+=1
                if nroot.right:
                    queue.append(nroot.right)
                    counter+=1
    
            counter2 = counter
            result.append(tempre)
            counter = 0
        return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.left = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
level = root.levelOrder(root)
print(level)