def LRUCache(strArr):
  arr=[]
  for item in strArr:
    if item not in arr and len(arr)<5:
      arr.append(item)
    elif item not in arr and len(arr)==5:
      arr.pop(0)
      arr.append(item)
    elif item in arr and len(arr)<=5:
      arr.remove(item)
      arr.append(item)
  st = ''
  for index,item in enumerate(arr):
    st = st +item
    if len(arr)-1!=index:
      st = st+'-'

    # code goes here 
  print(st)
    
LRUCache(["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]) 