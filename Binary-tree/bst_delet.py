class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
class BST:
  def insert(self,root,key):
    if root is None:
      return Node(key)

    if key<root.data:
      root.left = self.insert(root.left,key)
    else:
      root.right = self.insert(root.right,key)
    return root
  
  def delete(self,root,key):

    if root is None:
      return 

    if root.data>key:
      root.left = self.delete(root.left,key)
    elif root.data<key:
      root.right = self.delete(root.right,key)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp
      elif root.right is None:
        temp = root.left
        root = None
        return temp
      else:
        find_min = self.find_min(root.right)

        root.data = find_min.data

        self.delete(root.right,find_min.data)
    return root
  

  def find_min(self,root):
    temp = root
    while temp.left is not None:
      temp = temp.left
    return temp


  def inorder(self,root):
    if root is None:
      return
    self.inorder(root.left)
    print(root.data,end=' ')
    self.inorder(root.right)
root = Node(50)
bst = BST()
root = bst.insert(root,30)
root = bst.insert(root,20)
root = bst.insert(root,40)
root = bst.insert(root,70)
root = bst.insert(root,60)
root = bst.insert(root,80)
bst.inorder(root)
root = bst.delete(root,50)
bst.inorder(root)

