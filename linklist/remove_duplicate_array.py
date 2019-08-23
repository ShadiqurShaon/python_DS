# array = [1, 1, 2]
# newarray = {}
# for item in array:
#     if item not in newarray:
#         newarray[item] = item
# print(len(newarray))

# nums = [1, 1, 2, 1, 2, 1, 3, 3]
# unique_nums = []
# unique_nums.append(nums[0])
    
# n = len(nums)
# for i in range(1, n):
#     if nums[i] != nums[i-1]:
#         unique_nums.append(nums[i])

# print(len(unique_nums))


class dd:
        def compare2(self,list1,list2):
                list1_dict = {i:i for i in list1}
                
                for item in list2:
                        if item not in list1_dict:
                                print('false')

if __name__ == "__main__":
        dd= dd()
        list1 = [1, 2, 3, 4, 5]
        list2 = [7, 3, 4, 5]
        dd.compare2(list1,list2)

    