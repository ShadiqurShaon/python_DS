class Linklist:
  def __init__(self):
    self.head = None
  
  class Node(object):
    def __init__(self,data):
      self.data = data
      self.next = None
  
  def insert_data(self,data):
    return self.Node(data)

  def print_list(self):
    temp = self.head
    while(temp):
      print(temp.data)
      temp = temp.next

  def print_list2(self,list):
    temp = list
    while(temp):
      print(temp.data)
      temp = temp.next

  def swap(self):
    temp = None
    curr = self.head
    while(curr.next.next!= None):
      node1 = curr
      node2 = curr.next
      node1.next = None
      node2.next = node1
      
      # node1 = node2
      temp = node2
      
      curr = curr.next
    self.head = temp

llist = Linklist()
llist.head = llist.insert_data(14)
llist.head.next = llist.insert_data(20)
llist.head.next.next = llist.insert_data(13)
llist.head.next.next.next = llist.insert_data(12)
llist.head.next.next.next.next = llist.insert_data(15)
llist.head.next.next.next.next.next = llist.insert_data(10)
llist.print_list()
print("----------")
llist.swap()
llist.print_list()