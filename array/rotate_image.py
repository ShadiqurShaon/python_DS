def rotate(a):
  dic = {}
  print(len(a))
  for i in range(len(a)//2):
    a[i],a[(len(a)-1)-i]=a[(len(a)-1)-i],a[i]

  for i in range(len(a)):
    for j in range(len(a)):
      if i!=j and str([i,j]) not in dic:
        a[i][j],a[j][i]=a[j][i],a[i][j]
        dic[str([i,j])]=[i,j]
        dic[str([j,i])]=[j,i]
      # print(a[i][j])
  return a
arr = [[ 5, 1, 9,11,1],
  [ 2, 4, 8,10,2],
  [13, 3, 6, 7,3],
  [15,14,12,16,4],
  [1,2,3,4,5]]
print(rotate(arr))