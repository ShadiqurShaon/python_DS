def contain(arr):
  strat = 0
  length = len(arr)-1
  distance = len(arr)-1
  flag = 0
  result = 0
  temp_re = 0
  while(strat<length):
    first = arr[strat]
    last = arr[length]
    if first>=last:
      temp_re = last*distance 
      length-=1
    else:
      temp_re = first*distance
      strat+=1

    if temp_re>result:
      result = temp_re
    
    distance-=1
  return result

print(contain([1,8,6,2,5,4,8,3,5]))