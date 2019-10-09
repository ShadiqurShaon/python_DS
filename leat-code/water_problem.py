def find(arr):
  len_arr = len(arr)-1
  result = 0
  for i in range(len_arr//2):
   first = arr[i]
   last =  arr[len_arr-i]
   distance = len_arr-i
   if first>=last:
     temp = last*distance
   else:
     temp = first*distance
   if temp>result:
     result = temp
   return result
   

print(find([1,8,6,2,5,4,8,3,7]))