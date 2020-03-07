def make(arr,index,subarr):
    if index==len(arr):
        print(subarr)
    else:
        make(arr,index+1,subarr)

        make(arr,index+1,subarr+[arr[index]])
arr = [1,2,3,4]
make(arr,0,[])

