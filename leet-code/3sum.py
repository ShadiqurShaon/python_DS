def find_sum(array): 
    result = {}
    for index,first_item in enumerate(array):
        # print(first_item)
        temp_array = array[index+1:]
        for in2,second_item in enumerate(temp_array):
            # print(second_item,end='')
            temp = first_item+second_item
            temp2_arr = temp_array[in2+1:]
            if temp<=0:
                if abs(temp) in temp2_arr:
                    re = [first_item,second_item,abs(temp)]
                    re.sort()
                    # re_sort = re.sort()
                    if str(re) not in result:
                        result[str(re)] = re
            else:
                temp=temp - (2*temp)
                if temp in temp2_arr:
                    re = [first_item,second_item,temp]
                    re.sort()
                    if str(re) not in result:
                        result[str(re)] = re
    final = []
    for item in result.values():
        final.append(item)
    print(final)  

find_sum([-4,-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
# find_sum([-1, 0, 1, 2, -1, -4])
# find_sum([1,2,-2,-1])
# find_sum([3,-2,1,0])