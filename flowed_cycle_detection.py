class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = None

    def additem(self,data):
        temp_node = Node(data)
        temp_node.next = self.head
        self.head = temp_node

    def create_loop(self,n):
        first_node = self.head
        second_node = self.head

        for _ in range(1,n):
            second_node = second_node.next

        while(first_node.next != None):
            first_node = first_node.next

        first_node.next = second_node

    def cycle_detection(self):
        fast_list = self.head.next.next
        slow_list = self.head
        flag = 0
        while(slow_list.next != None):
            if(fast_list.data == slow_list.data):
                flag = 1
                break
            fast_list = fast_list.next
            slow_list = slow_list.next.next
        if flag==1:
            print('found')
        else:
            print('not found')

    def print(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__=="__main__":
    linklist = linklist()
    linklist.additem(5)
    linklist.additem(4)
    linklist.additem(3)
    linklist.additem(2)
    linklist.additem(1)
    # linklist.create_loop(2)
    linklist.cycle_detection()
    # linklist.print()
        
