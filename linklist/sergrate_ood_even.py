class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Linklist:
  def __init__(self):
    self.head = None
  
  def insert(self,data):
    newNode = Node(data)
    newNode.next = self.head
    self.head = newNode

  def print(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

  def segrate(self):
    main_link = self.head
    odd = None
    even = None
    while(main_link):
      prev = main_link.next
      if(main_link.data % 2 ==0):
        main_link.next = even
        even = main_link
      else:
        main_link.next = odd
        odd = main_link
      main_link = prev
      odd2= odd
    while(odd2.next != None):
      odd2 = odd2.next
    odd2.next = even
    self.head = odd
if __name__ == "__main__":
    linklist = Linklist()
    linklist.insert(17)
    linklist.insert(15)
    linklist.insert(8)
    linklist.insert(12)
    linklist.insert(10)
    linklist.insert(15)
    linklist.insert(4)
    linklist.insert(1)
    linklist.insert(7)
    linklist.insert(6)
    linklist.segrate()
    linklist.print()
