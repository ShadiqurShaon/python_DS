class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linklist:

    def __init__(self):
        self.head = None

    def insert(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def find_nth_from_last(self,position):
        first = self.head
        second = self.head
        for i in range(1,position+1):
            second = second.next
        while(second):
            first = first.next
            second = second.next

        print(first.data)


if __name__ == "__main__":
    print('orginal list')
    link = linklist()
    link.insert(5)
    link.insert(4)
    link.insert(3)
    link.insert(2)
    link.insert(1)
    link.print_list()
    print("n_th node from last:")
    link.find_nth_from_last(1)