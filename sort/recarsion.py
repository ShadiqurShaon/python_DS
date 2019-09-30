def marge_sorte(arr): 
  
  if len(arr)<2:
    return
  mid = len(arr)//2
  left = arr[:mid]
  right = arr[mid:]
  print(arr)
  marge_sorte(left)
  print(arr)
  marge_sorte(right)
      
  

marge_sorte([54,26,93,17,77,31,44,55,20])
  
# This code is contributed by 
# Smitha Dinesh Semwal 