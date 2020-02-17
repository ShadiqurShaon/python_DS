def subarray(arr,strat,end,result):
    if end==len(arr):
        return result
    elif strat>end:
        return subarray(arr,0,end+1,result)
    else:
        print(arr[strat:end+1])
        tem = arr[strat:end+1]
        result.append(tem)
        return subarray(arr,strat+1,end,result)
    return result

arr = [1,2,3,4]
print(subarray(arr,0,0,[]))