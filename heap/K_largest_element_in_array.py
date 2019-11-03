def makeMinhippy(arr,n,i):
    root = i
    left = 2*i+1
    right = 2*i+2
    if left<n and arr[i]>arr[left]:
        root = left
    if right<n and arr[root]>arr[right]:
        root = right
    if root!=i:
        arr[i],arr[root] = arr[root],arr[i]
        makeMinhippy(arr,n,root)
arr = [1, 23, 12, 9, 30, 2, 50]
n = len(arr)
for i in range(n,-1,-1):
    makeMinhippy(arr,n,i)
print(arr)
for i in range(0,3):
    # arr[0],arr[i] = arr[i],arr[0]
    print(arr.pop(0))
    makeMinhippy(arr,n-i,0)
print(arr)