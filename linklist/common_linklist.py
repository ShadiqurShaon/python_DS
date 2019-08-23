class Node:
  def __init__(self,data):
    self.data = data
    self.next = None
class Linklist:
  def print_lidt(self,link1,link2):
    dec = {}
    temp = None
    while(link1):
      dec[link1.data] = link1.data
      link1 = link1.next

    while(link2):
      pre = link2.next
      if(link2.data in dec):
        link2.next = temp
        temp = link2
        link2 = pre
      else:
        link2 = link2.next
    return temp
        

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node4.next = node5
    node3.next = node4
    node2.next =node3
    node1.next = node2

    node11 = Node(1)
    node21 = Node(2)
    node31 = Node(8)
    node41 = Node(5)
    node51 = Node(10)
    node41.next = node51
    node31.next = node41
    node21.next =node31
    node11.next = node21
    linklist = Linklist()
    result_list = linklist.print_lidt(node1,node11)
    while(result_list):
      print(result_list.data)
      result_list = result_list.next


