class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    self.count = 1

class AVL:
  def insert_node(self,root,node):
    if root==None:
      return
    if root.data==node:
      root.count+=1
      # return
    if root.data>node and root.left==None:
      root.left = Node(node)
    elif root.data>node and root.left!= None:
      self.insert_node(root.left,node)
    elif root.data<node and root.right==None:
      root.right = Node(node)
    elif root.data<node and root.right!= None:
      self.insert_node(root.right,node)
    # elif root.data ==node:
    #   root.count+=1
    return root

  def print_tree(self,tree):
    if tree==None:
      return 
    print(tree.data,tree.count,end='--')
    self.print_tree(tree.left)
    self.print_tree(tree.right)
    # 12, 10, 20, 9, 11, 10, 12, 12
root = Node(12)
avl = AVL()
newroot = avl.insert_node(root,10)
newroot = avl.insert_node(newroot,20)
newroot = avl.insert_node(newroot,9)
newroot = avl.insert_node(newroot,11)
avl.print_tree(newroot)
newroot = avl.insert_node(newroot,10)
newroot = avl.insert_node(newroot,12)
newroot = avl.insert_node(newroot,12)
print("==========")
avl.print_tree(newroot)


