def jump(arr,index):
<<<<<<< HEAD
  if index>=len(arr)-1:
    return True
  elif arr[index]==0:
    return False
  else:
    for i in range(1,arr[index]):
      return jump(arr,index+arr[index+i])
print(jump( [3,1,1,1],0))
=======
  m=0
  for index,item in enumerate(arr):
    if(index>m):
      return False
    if item+index>m:
      m=item+index
  return Tru
    
  
print(jump( [2,2,0,1,1],0))
>>>>>>> 997cde8ffaba62e549050ccd1f339297f98e53c4
