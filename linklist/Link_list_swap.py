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

  def swap(self,x,y):
    if x==y:
      return
    prevx= None
    currx= self.head
    while(currx.data != x and currx):
      prevx = currx
      currx = currx.next
    prevy = None
    curry = self.head
    while(curry.data != y and curry):
      prevy = curry
      curry = curry.next
    prevx.next = curry
    prevy.next = currx
    temp = curry.next
    curry.next = currx.next
    currx.next = temp


 
  
llist = Linklist()
llist.head = llist.insert_data(1)
llist.head.next = llist.insert_data(2)
llist.head.next.next = llist.insert_data(3)
llist.head.next.next.next = llist.insert_data(4)
llist.head.next.next.next.next = llist.insert_data(5)
llist.head.next.next.next.next.next = llist.insert_data(6)
llist.print_list()
print("----------")
llist.swap(2,5)
llist.print_list()