class Node:
  def __init__(self,data):
    self.data = data
    self.next=None

class Llist:
  def swap(self,listl):

    head = listl
    while(head.next):
      first = head
      second = head.next
      head.next = second.next
      second.next =first
      head = second
      head = head.next.next

root = Node(1)
root.next = Node(2)
root.next.next = Node(3)
root.next.next.next  = Node(4)
llist = Llist()
llist.swap(root) 

