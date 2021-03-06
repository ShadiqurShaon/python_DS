def generateMatrix(n):
    
    result = [[0 for i in range(n)] for j in range(n)]
    coord = [[(i,j) for j in range(n)] for i in range(n)]
    
    count = 1
    
    while coord:
        for x, y in coord.pop(0):
            result[x][y] = count
            count += 1
        coord = zip *coord[::-1]

    return result   

print(generateMatrix(5))