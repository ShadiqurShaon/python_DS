def matrix(mat):
  len1 = len(mat)
  len2 = len(mat[0])
  temp = []
  for i in range(len1):
    for j in range(len2):
      if mat[i][j]==0:
        temp.append([i,j])
  for item in temp:
    for i in range(len1):
      for j in range(len2):
        if i==item[0]:
          mat[i][j]=0
        if j==item[1]:
          mat[i][j]=0
  for item in mat:
    print(item)
  


  # print(temp)

matrix([[0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]])