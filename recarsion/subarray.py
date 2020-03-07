def make(arr,start,end):
    if end==len(arr):
        return
    if start>end:
        make(arr,0,end+1)
    else:
        print(arr[start:end+1])
        make(arr,start+1,end)

arr = [1,2,3]
make(arr,0,0)

