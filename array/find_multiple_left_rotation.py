def rotate(arr):
  n = len(arr)
  temp = arr[0]
  for i in range(0,n-1):
    arr[i] = arr[i+1]
  arr[n-1]=temp
  return arr

arr = [1,3,5,7,9]
for i in range(0,14):
  arr = rotate(arr)
print(arr)