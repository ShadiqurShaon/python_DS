class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Linklist:
  def __init__(self):
    self.head = None
  
  def insert(self,data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

  def head_to_tell(self):
    temp = self.head
    while(temp.next.next != None):
      temp = temp.next
    pt = temp.next
    temp.next = None
    pt.next = self.head
    self.head = pt

  def revarce(self):
    temp = self.head
    new = None
    while(temp):
      prev = temp.next
      temp.next = new
      new = temp
      temp = prev
    self.head = new
  
  def printList(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

if __name__ == "__main__":
    linklist = Linklist()
    linklist.insert(5)
    linklist.insert(4)
    linklist.insert(3)
    linklist.insert(2)
    linklist.insert(1)
    # linklist.insert(10)
    # linklist.printList()
    # linklist.revarce()
    # linklist.printList()
    linklist.head_to_tell()
    linklist.printList()