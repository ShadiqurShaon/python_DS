def makeHippyfy(arr,n,i):
	root = i
	left = 2*i+1
	right = 2*i+2
	if n>left and arr[i]<arr[left]:
		root = left
	if n>right and arr[root]<arr[right]:
		root = right
	if root!=i:
		arr[i],arr[root] = arr[root],arr[i]
		makeHippyfy(arr,n,root)

arr = [ 12, 11, 13, 5, 6, 7]
n = len(arr)
for i in range(n,-1,-1):
	makeHippyfy(arr,n,i)
print(arr)

for i in range(n-1,0,-1):
	arr[0],arr[i] = arr[i],arr[0]
	makeHippyfy(arr,i,0)
print(arr)



