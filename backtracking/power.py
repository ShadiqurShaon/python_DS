def spiralOrder(arr):
    row = len(arr)
    col = len(arr[0])
    fr=0
    fc=0
    lr=row-1
    lc=col-1
    i=0
    j=0
    counter =0
    plus =False
    minus = False
    while counter<row*col:
        print(arr[j][i])
        
        if i!=lc and j==fr:
            i+=1
        elif i==lc and j!=lr and fc!=lc:
            j+=1
        elif i!=fc and j==lr:
            i-=1
        elif i==fc and j!=fr and fc!=lc:
            j-=1
        elif fc==lc and j==fr:
            plus=True
        elif fc==lc and j==lr:
            minus=True
        if minus:
            j-=1
        elif plus:
            j+=1
        if j==lr and i==fc:
            fr+=1
            lc-=1
        if j!=lr and i!=lc and i==j:
            lr-=1
            fc+=1
   
        counter+=1


# def spiralOrder(matrix):
#     ret = []
#     while matrix:
#         ret += matrix.pop(0)
#         if matrix and matrix[0]:
#             for row in matrix:
#                 ret.append(row.pop())
#         if matrix:
#             ret += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 ret.append(row.pop(0))
#     return ret
        
         


    

# spiralOrder([
# [0  ,1  ,2  ,3  ,4],
# [15 ,16 ,17 ,18  ,5],
# [14 ,23 ,24 ,19  ,6],
# [13 ,22 ,21 ,20  ,7],
# [12 ,11 ,10  ,9  ,8]
# ])

spiralOrder([
[0  ,1  ,2  ,3  ,4],
[15 ,16 ,17 ,18  ,5],
[14 ,23 ,24 ,19  ,6],
[13 ,22 ,21 ,20  ,7],
[12 ,11 ,10  ,9  ,8]
])
# [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]
