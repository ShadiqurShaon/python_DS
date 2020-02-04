def gray_sequence(arr,n):
  flag = 2
  while(n>1 and flag<=n ):
    re = []
    final = arr+arr[::-1]
    for index,i in enumerate(final):
      if type(i) is list:
        temp = i.copy()
      else:
        temp = [i]

      if index<=(len(final)/2)-1:
        temp.insert(0,0)
      else:
        temp.insert(0,1)
      re.append(temp)
    flag+=1
    arr = re.copy()
  result = []
  for t_list in arr:
    res = int("".join(str(x) for x in t_list), 2) 
    result.append(res)
  return result





print(gray_sequence([0,1],40))
