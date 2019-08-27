def find_pivot(arr,low,high):
    if high<low:
        return -1
    if high==low:
        return low
    mid = int((low+high)/2)
    print(mid)
    if mid<high and arr[mid]>arr[mid+1]:
        return mid
    if mid>low and arr[mid]<arr[mid-1]:
        return (mid-1)
    if arr[low]>arr[mid]:
        return find_pivot(arr,low,mid)
    return find_pivot(arr,mid,high)

array = [5,6,7,8,9,10,1,2,3]

print(find_pivot(array,0,8))


