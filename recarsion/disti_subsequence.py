def subs(arr,index,sub,target,count):
  if index==len(arr):
    if len(sub)==1:
      count+=1
  else:
    subs(arr,index+1,sub,target,count)
    subs(arr,index+1,sub+[arr[index]],target,count)
  return count
print(subs([1,2,3],0,[],5,0))