class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BST:
  def inorder(self,root,li):
    if root is None:
      return
    self.inorder(root.left,li)
    print(root.data,end=' ')
    li.append(root.data)
    self.inorder(root.right,li)
    return li
    
  def preorder(self,root,li,i):
    if root is None:
      return
    i[0]+=1
    root.data = li[i[0]]
    self.preorder(root.left,li,i)
    self.preorder(root.right,li,i)

    return root

  def preorder2(self,root):
      if root is None:
        return
      print(root.data)
      self.preorder2(root.left)
      self.preorder2(root.right)


root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

bst = BST()
li = bst.inorder(root,[])
print('\n')
i = [-1] 
new_root = bst.preorder(root,li,i)

bst.preorder2(new_root)
