from queue import Queue
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self):
        self.root = None
        self.queue = Queue()

    def push_tree(self,data):
         new_node = Node(data)
         if self.root is None:
             self.root = new_node
             self.queue.put(self.root)
             
         else:
             recent_node = self.queue.get()

             if recent_node.left and recent_node.right is not None:
                 recent_node = self.queue.get()

             if recent_node.left is None:
                 recent_node.left = new_node
                 self.queue.put(recent_node)
                 self.queue.put(recent_node.left)

             elif recent_node.right is None:
                 self.queue.put(recent_node)
                 recent_node.right = new_node 
                 self.queue.put(recent_node.right)

    def print_tree(self):
       
        self.q = Queue()
        self.q.put(self.root)
        while(self.q.qsize()!=0):
            temp = self.q.get()
            print(temp.data)
            if temp.left != None:
                
                self.q.put(temp.left)
            if temp.right != None:
                
                self.q.put(temp.right)
    def print_hudai(self):
        temp = self.root
        print(temp.left.left.data)

if __name__ == "__main__":
    tree = Tree()
    tree.push_tree(1)
    tree.push_tree(2)
    tree.push_tree(3)
    tree.push_tree(4)
    tree.push_tree(5)

    tree.print_tree()
    tree.print_hudai()

