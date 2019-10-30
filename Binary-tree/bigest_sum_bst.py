class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def __init__(self):
    self.total = 0
  def inorder(self,root):
    if root==None:
      return
    self.inorder(root.left)
    print(root.data,end=' ')
    self.inorder(root.right)
    
  def re_inorder(self,root):
    if root==None:
      return
    self.re_inorder(root.right)
    self.total = self.total+root.data
    print(self.total,end='-')
    self.re_inorder(root.left)

root = Node(11)
root.left = Node(2)
root.right = Node(29)
root.left.left = Node(1)
root.left.right = Node(7)
root.right.left = Node(15)
root.right.right = Node(40)
root.right.right.left = Node(35)
bst = BST()
bst.inorder(root)
bst.re_inorder(root)
