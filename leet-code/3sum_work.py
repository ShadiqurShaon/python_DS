def find(arr):
  arr = sorted(arr)
  result = {}
  index = 0
  while(arr[index]<1):
    first = arr[index]
    target = 0-first
    l = index+1
    r = len(arr)-1
    while(l<r):
      if arr[l]+arr[r]==target:
        li = sorted([first,arr[l],arr[r]])
        if str(li) not in result:
          result[str(li)] = li 
        l+=1
        r-=1
      elif arr[l]+arr[r]<target:
        l+=1
      else:
        r-=1
    index+=1
  return result

re = find([-4,-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
for i in re.values():
  print(i)