def make(arr):
    re = None
    for i in range(len(arr)-1,-1,-1):
        if arr[i]>arr[i-1] and i-1!=-1:
            arr[i:] = sorted(arr[i:])
            j=i
            while(arr[i-1]>=arr[j]):
                j+=1
            arr[i-1],arr[j]=arr[j],arr[i-1]
            break
        if i==0:
            arr = sorted(arr)
    return arr
            

print(make([3,2,1]))
