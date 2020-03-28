def subset(arr,index,subs):
  if index==len(arr):
    print(subs)
    return
  
  if index<len(arr):
    subset(arr,index+1,subs)
    subset(arr,index+1,subs+[arr[index]])

def subarray(arr,start,end):
  if start==len(arr):
    return
  if start>end:
    subarray(arr,0,end+1)
  else:
    print(arr[start:end+1])
    subarray(arr,start+1,end)
subarray([1,2,3],0,0)