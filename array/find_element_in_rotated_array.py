def find_element(arr,key,low,high):
    if low>high:
        return
    mid = find_pivot(arr,low,high)
    if arr[mid] == key:
         return key
    if arr[0]<key:
        return binary_search(arr,key,low,mid)
    return binary_search(arr,key,mid+1,high)

def binary_search(arr,key,low,high):
    mid = int((low+high)/2)
    if arr[mid] == key:
        return mid
    if array[mid+1] == key:
        return (mid+1)
    if array[mid-1] == key:
        return (mid-1)
    if arr[low]>=arr[mid]:
        return binary_search(arr,key,low,mid-1)
    return binary_search(arr,key,mid+1,high)
        



def find_pivot(arr,low,high):
    if low>high:
        return
    if high == low:
        return low
    mid = int((low+high)/2)
    if mid<high and arr[mid]>arr[mid+1]:
        return mid
    if mid>low and arr[mid]<arr[mid-1]:
        return (mid-1)
    if arr[low]<arr[mid]:
        return find_pivot(arr,mid+1,high)
    return find_pivot(arr,low,mid-1)


array = [5,6,7,8,9,10,1,2,3]
print(find_element(array,8,0,8))

