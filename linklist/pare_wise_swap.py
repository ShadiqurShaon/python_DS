class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkllist:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def pare_wise_swap(self):
        
        dummy = Node(0)
        dummy.next = self.head
        temp = dummy
        while(temp.next and temp.next.next):
            first = temp.next
            sec = temp.next.next
            temp.next = sec
            first.next = sec.next
            sec.next = first
            temp = temp.next.next
        self.head = dummy.next



        
        # return temp

if __name__ == "__main__":
    list = Linkllist()

    list.insert(6)
    list.insert(5)
    list.insert(4)
    list.insert(3)
    list.insert(2)
    list.insert(1)
    # list.print_list()
    list.pare_wise_swap()
    print('------------')
    list.print_list()
        