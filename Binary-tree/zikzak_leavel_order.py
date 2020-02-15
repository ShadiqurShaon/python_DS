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
        booli = True
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
            if booli:
                result.append(tempre)
                booli = False
            else:
                result.append(tempre[::-1])
                booli = True
            counter = 0
        return result
root = Node(1)
root.left = Node(3)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(15)
root.left.left.right = Node(14)
root.left.right.left = Node(13)
root.left.right.right = Node(12)
root.right.left.left =Node(11) 
root.right.left.right =Node(10)
root.right.right.right = Node(8)
root.right.right.left  = Node(9) 

level = root.levelOrder(root)
print(level)