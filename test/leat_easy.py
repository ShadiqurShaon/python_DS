def transformArray(arr): 
  while(1):
      j = True
      arr_ref = arr.copy()
      for i in range(1,len(arr)-1):
          if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
              arr_ref[i]-=1
              j= False
          elif arr[i]<arr[i-1] and arr[i]<arr[i+1]:
              arr_ref[i]+=1
              j = False
      if j==True:
          break
      arr = arr_ref.copy()
  return arr 

print(transformArray([1,6,3,4,3,5]))