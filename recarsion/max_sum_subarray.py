def find(arr,strat,end,re):
    temp = sum(arr[strat:end+1])
    if temp>re:
        re = temp
    if end == len(arr):
        return re 
    if strat>end:
        return find(arr,0,end+1,re)
    else:
        return find(arr,strat+1,end,re)

arr = [-2, -3, 4, -1, -2, 1, 5, -3] 
print(find(arr,0,0,0))
