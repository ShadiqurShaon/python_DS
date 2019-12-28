def jump(arr,index):
    if index>=len(arr)-1:
        return True
    if arr[index]==0:
        return False
    rang = index+arr[index]
    for i in range(index,rang+1):
        val = jump(arr,i+arr[i])
        if val:
            return True
    return False

print(jump([3,0,2,0,1,2,0,0],0))