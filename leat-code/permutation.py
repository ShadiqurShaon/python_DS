class Solution:
    def __init__(self):
        self.result = []
    
    def permute(self, nums):
        
        self.per(nums,0,len(nums)-1,[])
        return self.result
        
    def per(self,a,s,r,result):
        if s==r:
            x = a
            result.append(x)
        else:
            for i in range(s,r+1):
                a[s],a[i] = a[i],a[s]
                self.per(a,s+1,r,result)
                a[s],a[i] = a[i],a[s]

cass = Solution();
print(cass.permute([1,2,3]))