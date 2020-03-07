def subArray(arr,index,sub,target,count):
    if index==len(arr):
        if(''.join(sub)==target):
            count+=1
            print(count)
    else:
        subArray(arr,index+1,sub,target,count)

        subArray(arr,index+1,sub+[arr[index]],target,count)

    return count


print(subArray('rabbbit',0,[],'rabbit',0))
