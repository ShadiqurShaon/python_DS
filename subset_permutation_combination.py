class Recar:
    def subArray(self,arr,start,end):
        if start==len(arr):
            return 
        if start>end:
            self.subArray(arr,0,end+1)
        else:
            print(arr[start:end+1])
            self.subArray(arr,start+1,end)
        
    def subarray_dfs(self,arr):
        win_side = 1
        for i in range(len(arr)):
            j=0
            while(j<len(arr)):
                print(arr[j:j+win_side])
                j+=1
                if j+win_side>len(arr):
                    break
            win_side+=1
    def subSequence(self,arr,index,sub):
        if index==len(arr):
            print(sub)
        else:
            self.subSequence(arr,index+1,sub)
            self.subSequence(arr,index+1,sub+[arr[index]])
    
    def subSequence_dfs(self,arr,sub):
        print(sub)
        for i in range(len(arr)):
            self.subSequence_dfs(arr[i+1:],sub+[arr[i]])
    def subsequenceCombination(self,arr,sub,k):
        if len(sub)==k:
            print(sub)
        for i in range(len(arr)):
            self.subsequenceCombination(arr[i+1:],sub+[arr[i]],k)
    def permutation(self,arr,start,end):
        if start==end:
            print(arr)
        for i in range(start,end+1):
            arr[i],arr[start] = arr[start],arr[i]
            self.permutation(arr,start+1,end)
            arr[i],arr[start] = arr[start],arr[i]



cla = Recar()
cla.subArray([1,2,3,4],0,0)
print("-----------------")
cla.subarray_dfs([1,2,3,4])
print('------------------')
cla.subSequence([1,2,3],0,[])
print('------------------')
cla.subSequence_dfs([1,2,3],[])
print('------------------')
cla.subsequenceCombination([1,2,3],[],2)
print('------------------')
cla.permutation([1,2,3],0,2)
