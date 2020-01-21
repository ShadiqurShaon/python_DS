def matrix(matrix):
    temp = []
    len_i = len(matrix)
    len_j = len(matrix[0])

    for i in range(len_i):
        for j in range(len_j):
            if matrix[i][j]==0:
                temp.append([i,j])
    
    for item in temp:
        for i in range(len_i):
            for j in range(len_j):
                if i==item[0]:
                    matrix[i][j]=0
                if j==item[1]:
                    matrix[i][j]=0
    for item in matrix:
        print(item)

matrix([
  [2,1,1,2,5,0],
  [0,4,1,2,5,6],
  [1,1,0,1,1,1],
  [2,3,1,5,5,6],
  [2,3,1,5,5,6],
  [2,3,1,5,5,6]
])