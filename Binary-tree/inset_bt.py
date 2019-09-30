class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def insertInBst(self,root,data=None):
    # root = p_root
    if root==None:
      return

    if root.data>data and root.left==None:
      root.left = Node(data)
    elif root.data>data and root.left!=None:
      self.insertInBst(root.left,data)
    elif root.data<data and root.right==None:
      root.right = Node(data)
    elif root.data<data and root.right!=None:
      self.insertInBst(root.right,data)

    return root

  def print_bst(self,root):
    if root==None:
      return
    print(root.data,end=' ')
    self.print_bst(root.left)
    self.print_bst(root.right)
root = Node(10)
root.left = Node(5)
root.right = Node(12)

bst = BST()
bst.print_bst(root)
new = bst.insertInBst(root,15)
bst.print_bst(new)







