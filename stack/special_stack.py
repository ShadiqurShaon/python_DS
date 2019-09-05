class special_stack:
  def __init__(self):
    self.stack = []
    self.min = 10000
    self.len = 0

  def push(self,data):
    self.stack.append(data)
    if self.min>=data:
      self.min = data
    self.len = len(self.stack)
    return self.stack


  def pop(self):
    self.stack.pop()
    self.min = min(self.stack)
    self.len = len(self.stack)
    return self.stack

  def isEmpty(self):
    if self.len == 0:
      return True


  # def isFull():
  def getMin(self):
    return self.min

if __name__ == "__main__":
    stack = special_stack()
    print(stack.push(18))
    stack.push(19)
    stack.push(29)
    stack.push(15)
    print(stack.push(16))
    print(stack.getMin())



    
