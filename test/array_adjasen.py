def sort(nums):
    for index,item in  enumerate(nums[:-1]):
        temp = 0
        val = nums[index]
        for i_item in range(index+1,len(nums)):
            if val>nums[i_item]:
                temp=i_item
                val = nums[i_item]
        if index<temp:
            temp2 = nums[index]
            nums[index] = nums[temp]
            nums[temp] = temp2
    return nums

print(sort([2,0,2,2,2,1,1,0,0,0,1,1,0]))

