class Meanstack:
  def __init__(self):
    self.stack = []
    self.min = 0

  def push(self,data):
    if len(self.stack)==0:
      self.stack.append(data)
      self.min = data
    else:
      if data>=self.min:
        self.stack.append(data)
      else:
        tempdata = 2*data - self.min
        self.stack.append(tempdata)
        self.min = data
    return self.stack

  def pull(self):
    if self.stack[0]>=self.min:
      self.stack.pop()
    else:
      self.min = 2*self.min - self.stack[0]
      self.stack.pop()

  def getmin(self):
    return self.min

  def getstack(self):
    return self.stack
if __name__ == "__main__":
    stack = Meanstack()
    print(stack.push(3))
    print(stack.push(5))
    print(stack.getmin())
    print(stack.push(2))
    print(stack.push(1))
