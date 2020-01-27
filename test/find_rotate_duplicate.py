def search(arr,min,max,target):

    mid = (min+max)//2
    if mid<=0 or mid>=len(arr)-1:
      return False
    if arr[mid]==target or arr[min]==target or arr[max]==target:
      return True
    elif arr[mid]>arr[min] and target<arr[mid] and target>arr[min]:
      return search(arr,min,mid,target)
    elif arr[mid]<arr[max] and target<arr[mid] and target>arr[max]:
      return search(arr,mid,max,target)
    elif target>arr[mid] and target>arr[min]:
      return search(arr,min,mid-1,target)
    elif target>arr[mid] and target<arr[min]:
      return search(arr,mid+1,max,target)
    elif arr[mid]==arr[min] or arr[mid]==arr[max]:
      return search(arr,min,max-1,target)
    
    return False


print(search([2, 0, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2],0,11,1))