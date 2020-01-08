def jump(arr,index):
  if index>=len(arr)-1:
    return True
  elif arr[index]==0:
    return False
  else:
    for i in range(1,arr[index]):
      return jump(arr,index+arr[index+i])
print(jump( [3,1,1,1],0))