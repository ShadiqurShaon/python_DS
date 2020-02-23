def find(array,start,end):
    if start==len(array):
        return 
    if start>end:
        return find(array,0,end+1)
    else:
        print(array[start:end+1])
        return find(array,start+1,end)


def givenSum(array,start,end,re):
    if sum(array[start:end+1])==re:
        return[start,end]
    if start==len(array):
        return []
    if start>end:
        return givenSum(array,0,end+1,re)
    else:
        return givenSum(array,start+1,end,re)



def findProduct(nums,start,end,re):
    temp = 1
    for x in nums[start:end+1]:
        temp*=x
    
    if temp>re:
        re = temp
    if start ==len(nums):
        return re
    if start>end:
        return findProduct(nums,0,end+1,re)
    else:
        return findProduct(nums,start+1,end,re)

arr = [-2,0,-1]
re = findProduct(arr,0,0,0)
print(re)
        
    

# arr = [10, 2, -2, -20, 10]
# result = givenSum(arr,0,0,-10)
# print(result)
# arr = [1,2,3]
# find(arr,0,0)
