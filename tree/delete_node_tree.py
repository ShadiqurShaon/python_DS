class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
class Tree:
  def __init__(self):
    self.head = None
  
  def inorder(self,tree):
    if tree == None:
      return 0
    self.inorder(tree.left)
    print(tree.data)
    self.inorder(tree.right)
   
  def rightMost(self,tree,key):
    

    if tree.left:
      if tree.left.data == key:
        tree.left = None
        return 0
      self.rightMost(tree.left,key)
    if tree.right:
      if tree.right.data == key:
        tree.right = None
        return 0
      self.rightMost(tree.right,key)


  def deletion(self,tree,key):
    
    if tree.data == key:
      return 0
    if tree == None:
      return 0
    q = []
    key_node = None
    q.append(root)
    while(len(q)!=0):
      temp = q.pop(0) 
      if temp.data == key:
        key_node = temp
      if temp.left:
        q.append(temp.left)
      if temp.right:
        q.append(temp.right)
    if key_node:   
      x = temp.data
      self.rightMost(tree,x)
      key_node.data = x
    return tree



tree = Tree()
root = Node(10)
root.left = Node(11)
root.left.left = Node(7)
root.left.right = Node(12)
root.right = Node(9)
root.right.left = Node(15)
root.right.right = Node(8)
newtree = tree.deletion(root,12)
tree.inorder(newtree)