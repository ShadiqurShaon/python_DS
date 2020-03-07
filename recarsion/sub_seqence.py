def subSequence(arr,index,subarr):
    if index==len(arr):
        print(subarr)
    else:
        subSequence(arr,index+1,subarr)

        subSequence(arr,index+1,subarr+[arr[index]])

    return 
arr = [1,2,3]
subSequence(arr,0,[])


