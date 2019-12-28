def maxSubArray(nums):
        ts = nums[0]
        rs = nums[0]
        
        for i in range(1,len(nums)):
            # if nums[i]>ts and nums[i]+rs<nums[i]:
            #     ts= nums[i]
            #     rs= nums[i]
            # elif nums[i]+rs>ts:
            #     ts = rs+nums[i]
            #     rs+=nums[i]
            # else:
            #     rs+=nums[i]
             rs = max(nums[i],nums[i]+rs)
             if rs>ts:
                 ts = rs
        return ts
print(maxSubArray([8,-19,5,-4,20]))