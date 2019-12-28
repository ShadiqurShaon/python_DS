def jump(arr,index):
  m=0
  for index,item in enumerate(arr):
    if(index>m):
      return False
    if item+index>m:
      m=item+index
  return True
    
  
print(jump( [2,2,0,1,1],0))