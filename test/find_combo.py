
def combination(arr,target,i,temp):
   if target==0:
      print(temp)
      return
   if arr[i]>target:
      return
   for i in range(i,len(arr)):
      if arr[i]<target:
         temp.append(arr[i])
         target = target-arr[i]
         combination(arr,target,i+1,temp)
   # combination(arr,target,i,temp)
   return

print(combination([1,2,7,6,1,5],8,0,[]))
           

