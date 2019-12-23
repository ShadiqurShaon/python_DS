def permuteUnique(nums):
    res = []
    nums.sort()
    dfs(nums, [], res)
    return res
    
def dfs(nums, path, res):
    if not nums:
        res.append(path)
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

print(permuteUnique([1,1,2]))







# def permute(a,l,r,result):
#     if l==r:
#         temp = a.copy()
#         if temp not in result:
#             result.append(temp)
#     else:
#         for i in range(l,r+1):
#             a[l],a[i]=a[i],a[l]
#             permute(a,l+1,r,result)
#             a[l],a[i]=a[i],a[l]
#     return result

# print(permute([1,1,2],0,2,[]))