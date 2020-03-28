def make(i):
  result = []
  if i==1:
    result.append([1])
  else:
    result.append([1])
    result.append([1,1])
    for i in range(3,i+1):
      temp_re = []
      prev = result[-1].copy()
      for j in range(i):
        if j==0:
          temp_re.append(1)
        elif j+1==i:
          temp_re.append(1)
        else:
          temp_re.append(prev[j]+prev[j-1])
      result.append(temp_re)
  return result

print(make(0))
  