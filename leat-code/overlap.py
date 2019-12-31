def overlap(intervals):
    arr = sorted(intervals, key=lambda x:x[0])
    result = []
    temp = []
    for item in arr:
        if not temp:
            temp=item
        else:
            if temp[1]>=item[0]:
                temp = [temp[0],max(temp[1],item[1])]
            else:
                result.append(temp)
                temp = item
    result.append(temp)
    return result
print(overlap([[5,10],[4,5]]))
