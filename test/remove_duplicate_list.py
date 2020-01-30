class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def print_list(self,list):
        
        while(list):
            print(list.data)
            list = list.next

    def remove(self,list):
        curr = list
        head=prev = Node(None)
        head.next = curr
        while(curr and curr.next):
            if curr.data == curr.next.data:
                while(curr and curr.next and  curr.data==curr.next.data):
                    curr = curr.next
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return head.next    

strat = Node(1)
strat.next = Node(1)
strat.next.next = Node(2)
strat.next.next.next = Node(3)
strat.next.next.next.next = Node(3)
strat.next.next.next.next.next = Node(4)
strat.next.next.next.next.next.next = Node(4)
strat.next.next.next.next.next.next.next = Node(5)
removed = strat.remove(strat)

strat.print_list(removed)

