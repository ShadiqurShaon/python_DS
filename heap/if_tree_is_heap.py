class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def check(self,root):
    queue = []
    queue.append(root)
    while(queue):
      temp = queue.pop(0)
      if temp.left is None or temp.right is None:
        return "not a heap"
      elif (temp.left is not None and temp.right is not None)and(temp.data<temp.left.data and temp.data<temp.right.data):
        return "not a heap"
        queue.append(temp.left)
        queue.append(temp.right)
      elif temp.left is None and temp.right is None:
        pass


        
