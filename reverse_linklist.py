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
    # linklist.printList()
    linklist.revarce()
    linklist.printList()