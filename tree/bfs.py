class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
class Tree:
  def bfs(self,tree):
    q = []
    q.append(tree)
    while(len(q)!=0):
      temp = q.pop(0)
      print(temp.data)
      if temp.left:
        q.append(temp.left)
      if temp.right:
        q.append(temp.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
tree = Tree()
tree.bfs(root)


