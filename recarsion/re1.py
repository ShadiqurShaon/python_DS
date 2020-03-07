def subarray(arr,start,end):
    if end==len(arr):
        return
    if start>end:
        return subarray(arr,0,end+1)
    else:
        print(arr[start:end+1])
        return subarray(arr,start+1,end)

subarray([1,2,3],0,0)