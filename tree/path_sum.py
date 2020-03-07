class Node:
  def __init__(self,data):
   self.data = data
    self.left = None
    self.right = None

class Tree:
  def find(self,root,sum):
    if not root:
      return
    if root.left==None and root.right==None and sum-root.data==0:
      return True
    sum -=root.data
    left =  self.find(root.left,sum)
    right = self.find(root.right,sum)

    if not left and not right:
      return False
    return True

root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(20)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(15)
tree = Tree()
print(tree.find(root,22))
