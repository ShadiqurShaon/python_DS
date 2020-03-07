class Linklist:
  def __init__(self,data):
    self.data = data
    self.next = None

class TreeNode:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class Tree:
  def make(self,llist):
    if not llist:
      return
    head=llist
    templist = llist
    lenth = 0
    while(head):
      lenth+=1
      head = head.next
    if lenth ==1:
      return TreeNode(llist.data)
    mid = lenth//2
    while(mid>1):
      templist = templist.next
      mid-=1
    root = TreeNode(templist.next.data)
    right = templist.next.next
    templist.next = None
    root.left = self.make(llist)
    root.right = self.make(right)
    return root

llist = Linklist(1)
llist.next = Linklist(2)
llist.next.next = Linklist(3)
llist.next.next.next = Linklist(4)
llist.next.next.next.next = Linklist(5)
tree = Tree()
print(tree.make(llist))
