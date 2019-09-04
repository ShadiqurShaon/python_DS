class hand_stack:
  def __init__(self):
    self.main_stack_container = []
  
  def push(self,data):
    self.main_stack_container.append(data)

  def pop(self):
    return self.main_stack_container.pop()

if __name__ == "__main__":
  newStack = hand_stack()
  newStack.push(1)
  newStack.push(2)
  newStack.push(-3)
  print(newStack.pop())
  print(newStack.pop())
  print(newStack.pop())

