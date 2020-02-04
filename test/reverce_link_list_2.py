class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def print_list(self,list):
        
        while(list):
            print(list.data)
            list = list.next

    def remove(self,head,m,n):
      ff = head
      fl = mf = ml = lf = None
      counter = 1
      while(head): 
        if counter==m-1:
          prev = head.next
          head.next = fl
          fl = head
          head = prev
        elif counter==n+1:
          lf = head
          head = head.next
        elif counter>=m and counter<=n:
          temp = head.next
          head.next = mf
          mf = head
          head = temp
        else:
          head = head.next
        counter+=1
      if mf is not None:
        ml = mf 
        while(ml.next):
          ml = ml.next
        ml.next = lf
      
      if fl is not None:
        fl.next = mf
      else:
         ff = mf
      return ff
      
           

strat = Node(1)
strat.next = Node(2)
strat.next.next = Node(3)
strat.next.next.next = Node(4)
strat.next.next.next.next = Node(5)
# strat.next.next.next.next.next = Node(4)
# strat.next.next.next.next.next.next = Node(4)
# strat.next.next.next.next.next.next.next = Node(5)
removed = strat.remove(strat,1,5)

strat.print_list(removed)