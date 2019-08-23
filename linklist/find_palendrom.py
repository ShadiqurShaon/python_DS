class Node:
    def __init__(self,data):
        self.data  = data
        self.next = None

class Link_list:
    def __init__(self):
        self.head = None

    def insert(self,data):
        tempNode = Node(data)
        tempNode.next = self.head
        self.head = tempNode
    
    def print_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def find_palendrom(self):
        current  = self.head
        stack = []
        while(current):
            stack.append(current.data)
            current = current.next
        current2 = self.head

        while(current2):
            if current2.data != stack.pop():
                return "not palendrom"
            current2 = current2.next
        return "palendrom"

    def remove_duplicate(self):
        current = self.head
        while(current.next != None):
            if current.data == current.next.data:
                current.next = current.next.next
                # current = current.next
            else:
                current = current.next


if __name__ == "__main__":
    llist = Link_list()
    llist.insert(1)
    llist.insert(1)
    llist.insert(2)
    llist.insert(2)
    llist.insert(3)
    llist.insert(3)

    llist.print_list()

    print("-------")
    llist.remove_duplicate()
    llist.print_list()

    
            