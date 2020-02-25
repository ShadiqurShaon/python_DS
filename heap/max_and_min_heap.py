class Heap:
    def hepifyForMax(self,arr,n,i):
        root = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[root]<arr[left]:
            root = left
        if right<n and arr[root]<arr[right]:
            root = right
        if root!=i:
            arr[root],arr[i] = arr[i],arr[root]
            return self.hepifyForMax(arr,n,root)
        return arr
    def hipipyForMin(self,arr,n,i):
        root = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[root]>arr[left]:
            root = left
        if right<n and arr[root]>arr[right]:
            root = right
        if root!=i:
            arr[root],arr[i] = arr[i],arr[root]
            self.hipipyForMin(arr,n,root)
    def makeMin(self,arr):
        n = len(arr)
        for i in range(n,-1,-1):
            self.hipipyForMin(arr,n,i)


    def makeMax(self,arr):
        n = len(arr)
        for i in range(n,-1,-1):
            self.hipipyForMin(arr,n,i)


