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
  
  def sorted_list_duplicate(self):
    temp = self.head
    while(temp.next != None):
      # print(temp.data)
      if temp.data == temp.next.data:

        temp.next = temp.next.next
      else:
        temp = temp.next

  def remove_duplicate_unsorted(self):
    dic = {}
    temp = self.head
    temp2 = None

    while(temp.next!=None):
      prev = temp.next
      if temp.data not in dic:
        dic[temp.data] = temp.data
        temp.next = temp2
        temp2 = temp
        temp = prev
      else:
        # temp.next = temp.next
        temp = prev
    self.head = temp2
  def print_List(self):
    temp_node = self.head
    while(temp_node):
      print(temp_node.data)
      temp_node = temp_node.next

if __name__ == "__main__":
    linklist = Linklist()
    linklist.insert(6)
    linklist.insert(6)
    linklist.insert(6)
    linklist.insert(5)
    linklist.insert(4)
    linklist.insert(6)
    linklist.insert(6)
    linklist.insert(1)

    # linklist.sorted_list_duplicate()
    linklist.remove_duplicate_unsorted()
    linklist.print_List()

