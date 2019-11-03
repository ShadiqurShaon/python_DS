class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linklist:
    def printList(self,head):
        while(head):
            print(head.data,end=' ')
            head = head.next
        print('')
    def removefromLast(self,n,head):
        headp = head
        headr = head
        for i in range(0,n+1):
            headp = headp.next
        while(headp):
            headp = headp.next
            headr = headr.next
        headr.next = headr.next.next
        return head
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
li = linklist()
li.printList(head)
r_li = li.removefromLast(2,head)
li.printList(r_li)