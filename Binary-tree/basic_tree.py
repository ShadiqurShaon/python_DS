class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def __init__(self):
    self.root = Node(0)
    
  def incert_tree(self,tree):
    stack = []
    stack.append(tree)
    tr = tree
    while(len(stack)!= 0):
      tr = stack.pop()

      if tr.left!=None:
        stack.append(tr.left)
      elif tr.right != None:
        stack.append(tr.right)
      elif tr.left == None:
        tr.left = Node(12)
        break
      elif tr.right== None:
        tr.right = Node(12)
        break

    return tree

    
  def print_tree(self,tree):

    if tree==None:
      return 0
    self.print_tree(tree.left)
    print(tree.data)
    self.print_tree(tree.right)
    



root = Node(10)
root.left = Node(11)
root.right = Node(9)
root.left.left = Node(7)
root.right.left = Node(15)
root.right.right = Node(8)
tree = Tree()
root2 = tree.incert_tree(root)
tree.print_tree(root2)
# tree.print_tree(root)
    
