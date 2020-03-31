def longest_palendrom(s):
  stack = []
  stack.append(s[0])
  ptr = 1
  result = [0]
  while(len(stack) != 0 ):
    temp = 0
    copy_stack = stack.copy()
    if ptr<len(s):
      for i in range(len(stack)):
        if copy_stack.pop() != s[ptr+i]:
          del stack[0]
          stack.append(s[ptr])
          ptr= ptr+1
          break
        temp+=1
    if len(result)<=len(stack):
      result = stack.copy()

    if temp == len(stack):
      for i in range(temp):
        stack.append(s[ptr])
        ptr = ptr+1
    else:
      del stack[0]
  return result
print(longest_palendrom('babad'))
    
