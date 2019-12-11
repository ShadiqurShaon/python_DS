def rotate(a):
  dic = {}
  for i in range(len(a)):
    for j in range(len(a)):
      if i!=j and str([i,j]) not in dic:
        a[i][j],a[j][i]=a[j][i],a[i][j]
        dic[str([i,j])]=[i,j]
        dic[str([j,i])]=[j,i]
      # print(a[i][j])
  return a
arr = [[1,2,3],
      [1,2,3],
      [1,2,3]]
print(rotate(arr))