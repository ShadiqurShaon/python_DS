class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.next = None
class Tree:
    def populate(self,root):
        queue = []
        result = []
        result.append(root)
        queue.append(root)
        while queue:
            temp_queue = []
            while queue:
                temp = queue.pop(0)
                if temp.left:
                    temp_queue.append(temp.left)
                if temp.right:
                    temp_queue.append(temp.right)
            queue = temp_queue
            for i in range(len(temp_queue)-1):
                temp_queue[i].next = temp_queue[i+1]
            result.append('#')
            for item in range(len(temp_queue)):
                result.append(queue.pop(0))
            queue = temp_queue
        return result
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

tree = Tree()
new_root = tree.populate(root)


        
