class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Linklist:
  def rotate(self,link):
    for i in range(2000000000):
      head = link
      while(link.next.next):
        # print(link.data)
        link = link.next
      last = link.next
      link.next = None
      last.next = head
      link = last
    while(last):
      print(last.data)
      last=last.next

    # print(last.data)


node = Node(1)
node.next = Node(2)
node.next.next = Node(3)
# node.next.next.next = Node(4)
# node.next.next.next.next = Node(5)
linklist = Linklist()
linklist.rotate(node)

