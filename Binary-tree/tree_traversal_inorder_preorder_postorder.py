class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = Node(0)

  def preorder(self,tree):
    #Root->Left->Right
    if tree==None:
      return 0
    print(tree.data)
    self.preorder(tree.left)
    self.preorder(tree.right)
    
     
  def inorder(self,tree):
    # Left->Root->Right
    if tree==None:
      return 0
    self.inorder(tree.left)
    print(tree.data)
    self.inorder(tree.right)
  
  def postorder(self,tree):
    #Left->Right->Root
    if tree==None:
      return 0
    self.postorder(tree.left)
    self.postorder(tree.right)
    print(tree.data)
    
    
root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)
tree = Tree()
# tree.inorder(root)
# tree.preorder(root)
tree.postorder(root)

    
