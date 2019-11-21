
def binarySearch(arr,key,min,max):
    if key<=arr[max]:
        mid = int((min+max)/2)
        if arr[mid]==key:
            return mid
        if arr[mid]>key:
            return binarySearch(arr,key,min,mid-1)
        else:
            return binarySearch(arr,key,mid+1,max)
    else:
        return -1


def findpivot(arr,min,max):
    if min>max:
        return 0
    if min==max:
        return min
    mid = int((min+max)/2)
    if mid>min and arr[mid]<arr[mid-1]:
        return mid-1
    elif mid<max and arr[mid]>arr[mid+1]:
        return mid
    elif arr[mid]>arr[min]:
        return findpivot(arr,mid,max)
    elif arr[mid]<arr[min]:
        return findpivot(arr,min,mid)
    else:
        return -1


arr = [40,50,-6,-5,8,9,10]
min = 0
max = len(arr)-1
key = 50
piv = findpivot(arr,min,max)
if piv!=-1:
    if arr[piv] == key:
        print(piv)
    elif arr[min]>key:
        print(binarySearch(arr,key,piv+1,max))
    else:
        print(binarySearch(arr,key,min,piv))
else:
    print(binarySearch(arr,key,min,max))
# arr = [ 2, 3, 4, 10, 40 ] 
# x = 2
# print(binarySearch(arr,x, 0, len(arr)-1)) 


