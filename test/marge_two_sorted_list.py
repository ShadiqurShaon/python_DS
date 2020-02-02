class Node:
  def __init__(self,data):
    self.data=data
    self.next = None
  def marge(self,nums1,nums2):
    prehead = Node(None)
    prehead.next = nums1
    while(prehead.next and nums2):
      if prehead.next.data>=nums2.data:
        pre2 = nums2.next
        nums2.next = prehead.next
        prehead.next = nums2
        prehead = prehead.next
        nums2 = pre2
      else:
        prehead = prehead.next
    return nums1

   

  def print_node(self,node):
    while(node):
      print(node.data)
      node = node.next


first = Node(1)
first.next = Node(3)
first.next.next = Node(5)
first.next.next.next = Node(7)
first.next.next.next.next = Node(11)

second = Node(2)
second.next = Node(4)
second.next.next = Node(6)
second.next.next.next = Node(8)
root = first.marge(first,second)
first.print_node(root)
