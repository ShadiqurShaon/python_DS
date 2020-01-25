# def remove(arr):
#   start = 1
#   counter = 1
#   check = arr[0]
#   result = 1
#   while(start<len(arr)):
#     if check ==arr[start] and counter<2:
#       result+=1
#       start+=1
#       counter+=1
#     elif check!=arr[start]:
#       check = arr[start]
#       start+=1
#       result+=1
#       counter=1
#     else:
#       start+=1
#   return result

def remove(nums):
  check =100000
  counter=0
  length = len(nums)
  for i in range(0,length):
    first = nums.pop(0)
    if (first==check and counter<2):
      nums.append(first)
      counter+=1
      check=first 
    elif(first!=check):
      nums.append(first)
      counter = 1
      check = first
    
  return len(nums)





print(remove([0,0,1,1,1,1,2,3,3]))