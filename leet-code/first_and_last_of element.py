def BinarySearch(arr,min,max,key):
    if (arr[min]<=key and arr[max]>=key)and(min>=0 and max<=len(arr)-1):
        if arr[min]==key:
            return min
        elif arr[max]==key:
            return max
        mid = (min+max)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]>key:
            return BinarySearch(arr,min,mid-1,key)
        elif arr[mid]<key:
            return BinarySearch(arr,mid+1,max,key)
        else:
            return -1
    else:
        return -1

def findstartend(arr,strt,end,key):
    while(1):
        if(strt==0 and end==len(arr)-1)or(strt==0 and arr[end+1]!=key)or(end==len(arr)-1 and arr[strt-1]!=key):
            break
        if(arr[strt-1]!=key and arr[end+1]!=key):
            break
        if strt-1>=0 and arr[strt-1]==key:
            strt-=1
        if end+1<len(arr) and arr[end+1]==key:
            end+=1
    return [strt,end]

arr = [1,1,1,1,8]
max = len(arr)-1
pos = BinarySearch(arr,0,max,7)
print(pos)
# print(findstartend(arr,pos,pos,8))


