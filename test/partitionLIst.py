class Node:
  def __init__(self,data):
    self.data=data
    self.next = None
  def RemoveD(self,node,target):
    equal_head = equal_last = None
    less_head = less_last = None
    greter_head = gretter_last = None

    while(node):
      # if node.data==target:
      #   if equal_last is None:
      #     equal_head = equal_last = node
      #   else:
      #     equal_last.next = node
      #     equal_last = equal_last.next
      if node.data<target:
        if less_head is None:
          less_head = less_last = node
        else:
          less_last.next = node
          less_last = less_last.next
      else:
        if gretter_last is None:
          greter_head = gretter_last = node
        else:
          gretter_last.next = node
          gretter_last = gretter_last.next
        
          

      node = node.next
  
    # gretter_last.next = None
    # equal_last.next=greter_head
    # less_last.next = equal_head
    gretter_last.next = None
    less_last.next = greter_head
    return less_head






  def print_node(self,node):
    while(node):
      print(node.data)
      node = node.next


start = Node(1)
start.next = Node(4)
start.next.next = Node(3)
start.next.next.next = Node(2)
start.next.next.next.next = Node(5)
start.next.next.next.next.next = Node(2)
start.next.next.next.next.next.next = Node(1)
root = start.RemoveD(start,3)
start.print_node(root)
