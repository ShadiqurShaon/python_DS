def subarray(arr,sum):
    last_sum = sum
    re = []
    index = 0
    while 1:
        if arr[index]<=last_sum:
            last_sum-=arr[index]
            re.append(index)
            index+=1
        elif arr[index]>last_sum and last_sum>0:
            last_sum+=arr[re[0]]
            del re[0]
            last_sum-=arr[index]
            re.append(index)
            index+=1
        elif last_sum<0:
            last_sum+=arr[re[0]]
            del re[0]

        if last_sum==0:
            break
        if last_sum!=0 and index==len(arr):
            return -1
    print(re)
        

subarray([1 ,2 ,3 ,8 ,5],12)
            
