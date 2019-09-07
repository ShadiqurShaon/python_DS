class Node:
  def __init__(self,data):
    self.data = data
    self.next = None

class Marge_stack:
  def __init__(self):
    self.s1 = None
    self.s2 = None
    self.temps1 = None
    self.temps2 = None

  def push1(self,data):
    new_node = Node(data)
    new_node.next = self.s1
    self.s1 = new_node
    self.temps1 = self.s1
    while(self.temps1.next != None):
      self.temps1 = self.temps1.next

  def push2(self,data):
    new_node = Node(data)
    new_node.next = self.s2
    self.s2 = new_node
    self.temps2 = self.s2
    while(self.temps2):
      self.temps2 = self.temps2.next

  def marge(self,s1,s2):
   first = s1.temps1
   second = s2.s1
   first.next = second
   final = s1.s1
  
  #  while(final):
  #    print(final.data)
  #    final = final.next
   return final
if __name__ == "__main__":
    list1 =  Marge_stack()
    list1.push1(1)
    list1.push1(2)
    list1.push1(3)
    list2 = Marge_stack()
    list2.push1(4)
    list2.push1(5)
    list2.push1(6)
    newlist = Marge_stack()
    link = newlist.marge(list1,list2)
    while(link):
      print(link.data)
      link = link.next
  
