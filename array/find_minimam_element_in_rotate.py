def find_min(arr,low,high):
    if high<low:
        return arr[0]
    if high == low:
        return arr[low]

    mid = int((low+high)/2)

    if high>mid and arr[mid+1]<arr[mid]:
        return arr[mid+1]
    if mid>low and arr[mid]<arr[mid-1]:
        return arr[mid]
    if arr[high]>arr[mid]:
        return find_min(arr,low,mid-1)
    return find_min(arr,mid+1,high) 

arr = [5,6,7,8,9,10,1,2,3]
print(find_min(arr,0,8))

arr1 = [5, 6, 1, 2, 3, 4] 
n1 = len(arr1) 
print("The minimum element is " + str(find_min(arr1, 0, n1-1))) 
  
arr2 = [1, 2, 3, 4] 
n2 = len(arr2) 
print("The minimum element is " + str(find_min(arr2, 0, n2-1))) 
  
arr3 = [1] 
n3 = len(arr3) 
print("The minimum element is " + str(find_min(arr3, 0, n3-1))) 
  
arr4 = [1, 2] 
n4 = len(arr4) 
print("The minimum element is " + str(find_min(arr4, 0, n4-1))) 
  
arr5 = [2, 1] 
n5 = len(arr5) 
print("The minimum element is " + str(find_min(arr5, 0, n5-1))) 
  
arr6 = [5, 6, 7, 1, 2, 3, 4] 
n6 = len(arr6) 
print("The minimum element is " + str(find_min(arr6, 0, n6-1))) 
  
arr7 = [1, 2, 3, 4, 5, 6, 7] 
n7 = len(arr7) 
print("The minimum element is " + str(find_min(arr7, 0, n7-1))) 
  
arr8 = [2, 3, 4, 5, 6, 7, 8, 1] 
n8 = len(arr8) 
print("The minimum element is " + str(find_min(arr8, 0, n8-1))) 
  
arr9 = [3, 4, 5, 1, 2] 
n9 = len(arr9) 
print("The minimum element is " + str(find_min(arr9, 0, n9-1)))