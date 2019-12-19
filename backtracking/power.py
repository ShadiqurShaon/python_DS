def spiral(arr):
    row = len(arr)
    col = len(arr[0])
    fr=0
    fc=0
    lr=4
    lc=4
    cont = 1
    i=0
    j=0
    while 1:
        print(arr[j][i])
        if i!=lc and j==fr:
            i+=1
        elif i==lc and j!=lr:
            j+=1
        elif i!=fc and j==lr:
            i-=1
        elif i==fc and j!=fr:
            j-=1
        if j==lr and i==fc:
            fr+=1
            lc-=1
        if j!=lr and i!=lc and i==j:
            lr-=1
            fc+=1
         


    print(row,col)

spiral([
[0  ,1  ,2  ,3  ,4],
[15 ,16 ,17 ,18  ,5],
[14 ,23 ,24 ,19  ,6],
[13 ,22 ,21 ,20  ,7],
[12 ,11 ,10  ,9  ,8]
])
  

