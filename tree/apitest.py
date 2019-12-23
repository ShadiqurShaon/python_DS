def jump(arr,index):
  if index>=len(arr):
    return True
  elif arr[index]==0:
    return False
  else:
    if index==0:
      return jump(arr,arr[0])
    else:
      return jump(arr,index+arr[index])
print(jump( [2,0,1],0))