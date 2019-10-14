class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class Main:
  def inorder(self,root):
    if root==None:
      return
    self.inorder(root.left)
    print(root.data,end=' ')
    self.inorder(root.right)

  def insert_in_array(self,root,array):
    if root==None:
      return
    self.insert_in_array(root.left,array)
    array.append(root.data)
    self.insert_in_array(root.right,array)
    return array
  
  def convert_bt_array(self,root):
    array = []
    converted = self.insert_in_array(root,array)
    converted.sort()
    root = self.bt_to_bst_convert(root,converted)
    self.inorder(root)
  
  def bt_to_bst_convert(self,root,array):
    if root == None:
      return
    self.bt_to_bst_convert(root.left,array)
    root.data = array.pop(0)
    self.bt_to_bst_convert(root.right,array)

    return root


root = Node(10)
root.left = Node(30)
root.right = Node(15)
root.left.left = Node(20)
root.right.right = Node(5)
main = Main()
main.convert_bt_array(root)

# main.inorder(root)
