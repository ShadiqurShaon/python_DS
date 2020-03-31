def daylist(arr):
    if not arr:
        return
    result = []
    for index,item in enumerate(arr):
        counter=index+1
        dif = 1
        for indexrest,itemrest in enumerate(arr[index+1:]):
            if itemrest>item:
                result.append(dif)
                break
            dif+=1
            counter+=1
        if counter>=len(arr):
            if arr[index]<=item:
                result.append(0)


    return result


def st(T):
    res, stack = [0] * len(T), []
    for i in range(len(T)):
        while stack and T[stack[-1]] < T[i]:
            res[stack.pop()] = i - stack[-1]
        stack.append(i)
    return res
t = [73, 74, 75, 71, 69, 72, 76, 80]

print(st(t))
