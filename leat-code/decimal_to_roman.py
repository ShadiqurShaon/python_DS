def calculate(num):
  result = []
  while num!=0:
    if num<4:
      result.append(num)
      num=0
    elif num==4:
      result.append(num)
      num=0
    elif num<9:
      result.append(num//5)
      num = num%5
    elif num==9:
      result.append(num)
    elif num<49:
      result.append(num//10)
      num = num%10
    elif num==49:
      result.append(num)
    elif num<99:
      result.append(num//50)
      num = num%50


  return result

print(calculate(29))
