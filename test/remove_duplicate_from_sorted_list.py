class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def print_list(self,list):
        
        while(list):
            print(list.data)
            list = list.next

    def remove(self,list):
        head = list
        head2 = head.next
        while(head2):
            if head.data!=head2.data:
                head.next = head2
                head = head.next
                head2 = head2.next
            else:
                head2 = head2.next
        head.next = head2
        return list


strat = Node(1)
strat.next = Node(1)
strat.next.next = Node(2)
strat.next.next.next = Node(3)
strat.next.next.next.next = Node(3)
strat.next.next.next.next.next = Node(4)
strat.next.next.next.next.next.next = Node(5)
strat.next.next.next.next.next.next.next = Node(5)
removed = strat.remove(strat)

strat.print_list(removed)

