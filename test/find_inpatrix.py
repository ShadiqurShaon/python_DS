def matrix(matrix,target):
    col_min = 0
    col_max = len(matrix)
    find_col = 0
    if len(matrix)>1:
        while(1):
            mid = (col_min+col_max)//2
            if matrix[mid][0]==target:
                find_col= mid
                break
            elif matrix[mid][0]<target and matrix[mid+1][0]>target :
                find_col= mid
                break
            elif matrix[mid][0]>target and matrix[mid-1][0]<=target:
                find_col= mid-1
                break
            elif matrix[mid+1][0]<target and mid+1>=len(matrix)-1:
                find_col= mid+1
                break
            elif matrix[0][0]>target:
                find_col= 0
                break
            elif matrix[mid][0]<target:
                col_min = mid+1
            elif matrix[mid][0]>target:
                col_max=mid-1
    else:
        find_col = 0
    min=0
    max = len(matrix[find_col])
    while(min<max):
        mid = (min+max)//2
        if matrix[find_col][mid]==target:
            return True
        elif matrix[find_col][mid]<target:
            min=mid+1
        elif matrix[find_col][mid]>target:
            max=mid-1
    return False

        



    # col = 0
    # for index,item in enumerate(matrix):
    #     if item[0]>s_item:
    #         col=index-1
    #         break
    # for item in matrix[col]:
    #     if item==s_item:
    #         return "Found"

    # return "Not Found"

print(matrix([
  [2,   3,  5,  7],
  [12,   13,  15,  17],
  [22,   23,  25,  27],
  [32,   33,  35,  37]
 
],1))
