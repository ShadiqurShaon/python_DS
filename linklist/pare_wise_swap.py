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
        temp = self.head
        prev = None
        while(temp):
            n2 = temp.next
            temp.next = temp.next.next
            n2.next = temp
            temp = n2
            n2.next = prev
            prev = n2
            temp = temp.next.next
        self.head = prev
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
        