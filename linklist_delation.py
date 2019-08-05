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

    def insert_at_end(self,data):
        newNode = Node(data)
        temp = self.head
        while(temp.next!=None):
            temp = temp.next
        temp.next = newNode
        
    def insert_after(self,aftervalue,inserted_value):
        newNode = Node(inserted_value)
        temp = self.head
        while(temp!=None):
            if temp.data == aftervalue:
                break            
            temp = temp.next
        newNode.next = temp.next
        temp.next = newNode

    def deleteNode(self,data):
        temp = self.head
        while(temp.next!=None):
            if temp.next.data == data:
                break
            temp = temp.next
        temp.next = temp.next.next

    def delete_in_position(self,position):
        temp = self.head
        if position == 1:
            temp = temp.next
            self.head = temp
        else:
            count = 1
            while(temp.next != None):
                if count == position-1:
                    break
                temp = temp.next
                count+=1
            temp.next = temp.next.next 



    def print_list(self):
        temp = self.head
        while(temp!=None):
            print(temp.data)
            temp = temp.next
if __name__ == "__main__":
    linklist = linklist()
    linklist.insert_in_begining(3)
    linklist.insert_in_begining(2)
    linklist.insert_at_end(4)
    linklist.insert_in_begining(1)
    linklist.insert_after(2,5)
    linklist.print_list()
    
    print('------')

    linklist.delete_in_position(5)
    linklist.print_list()
    # linklist.deleteNode(5)
    # linklist.print_list()

        