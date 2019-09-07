from queue import Queue 

class stack_with_queue:
  def __init__(self):
    self.q1 = Queue()
    self.q2 = Queue()

  def enque(self,data):
    
    while(not self.q1.empty()):
      self.q2.put(self.q1.queue[0])
      self.q1.get()
      
    
    self.q1.put(data)
    while(not self.q2.empty):
      self.q1.put(self.q2.queue[0])
      self.q2.get()
      
    

  def deque(self):
    return self.q1.get()

if __name__ == "__main__":
    que = stack_with_queue()
    que.enque(20)
    que.enque(30)
    que.enque(40)
    print(que.deque())
    # print(que.deque())
    # print(que.deque())

