def find(arr):
    arr.sort()
    result = {}
    index = 0
    while(arr[index]<1):
        first = arr[index]
        last_index = len(arr)-1
        second_index = index+1
        while(1):
            second = arr[second_index]
            if first+second+arr[last_index]==0:
                li = [first,second,arr[last_index]]
                li.sort()
                if str(li) not in result:
                    result[str(li)] = li
                # break
            if second_index == len(arr)-2:
                break
            if arr[last_index]<1 or second_index+1==last_index:
                second_index+=1
                last_index = len(arr)-1
            else:
                last_index-=1
        index+=1
    return result

# array = find([-4,-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
# array = find([-1, 0, 1, 2, -1, -4])
# array = find([3,-2,1,0])
# array = find([0,0,0])
array = find([-14,-3,11,-3,12,-1,11,13,5,6,-11,-14,-6,11,-4,-15,3,-15,9,-10,13,-10,-9,-13,-12,12,-7,12,12,3,9,5,-14,-3,9,13,11,5,3,-6,-12,-1,-5,-3,-4,-2,-10,6,-10,14,3,-11,11,10,-9,7,-1,-9,4,-12,2,-2,8,3,3,-6,-7,-1,6,12,8,9,-12,10,-8,-1,-7,-3,12,-9,-12,1,-5,6,-12,-7,-2,2,-8,-13,5,9,-7,-10,-3,11,-1,-3,-13,-10,-14,11,6,-10,6,13,4,7,-13,-6,13,12,10,-15,4,13,-7,9,-8,0,4,4,-6,12,9,-2,0])
for i in array.values():
    print(i)