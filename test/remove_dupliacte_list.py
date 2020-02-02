class Node:
  def __init__(self,data):
    self.data=data
    self.next = None
  def RemoveD(self,node):
    head1 = node
    head2 = node.next
    while(head2):
      
      if head1.data!=head2.data:
        head1.next = head2
        head1 = head1.next
        head2 = head2.next
      else:
        head2 = head2.next
      # node = node.next
    return node

  def print_node(self,node):
    while(node):
      print(node.data)
      node = node.next


start = Node(1)
start.next = Node(2)
start.next.next = Node(3)
start.next.next.next = Node(3)
start.next.next.next.next = Node(4)
start.next.next.next.next.next = Node(5)
root = start.RemoveD(start)
start.print_node(root)
