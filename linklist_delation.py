class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def insert_in_begining(self,data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def print_list(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next
if __name__ == "__main__":
    linklist = linklist()
    linklist.insert_in_begining(3)
    linklist.insert_in_begining(2)
    linklist.insert_in_begining(1)
    linklist.print_list()

        