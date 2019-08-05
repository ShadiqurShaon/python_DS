array = [1, 1, 2]
newarray = {}
for item in array:
    if item not in newarray:
        newarray[item] = item
print(len(newarray))

# nums = [1, 1, 2, 1, 2, 1, 3, 3]
# unique_nums = []
# unique_nums.append(nums[0])
    
# n = len(nums)
# for i in range(1, n):
#     if nums[i] != nums[i-1]:
#         unique_nums.append(nums[i])

# print(len(unique_nums))