class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None
    
    def insert_node(self,data,list_all):
        newnode = Node(data)
        newnode.next = list_all
        list_all = newnode
        return list_all
    
    def return_linklist(self):
        return self.head

    
    def marge_link_list(self,list1,list2):

        while(list1):
            prev1 = list1.next
            prev2 = list2.next
            if(list1.data >= list2.data):
                list1.next = self.head
                self.head = list1
                list2.next = self.head
                self.head =list2 
                            
            else:
                list2.next = self.head
                self.head = list2
                list1.next = self.head
                self.head = list1

            
            list2 = prev2
            list1 = prev1
        print('out')
        return self.head

    def print_list(self,list_print):
        temp = list_print
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    link_list1 = Linklist()
    node1 = Node(4)
    el1 = link_list1.insert_node(2,node1)
    el2 = link_list1.insert_node(1,el1)

    node2 = Node(4)
    nel1 = link_list1.insert_node(3,node2)
    nel2 = link_list1.insert_node(1,nel1)

    link_list1.print_list(nel2)
    link_list1.print_list(el2)

    final_list = link_list1.marge_link_list(el2,nel2)
    link_list1.print_list(final_list)



    

