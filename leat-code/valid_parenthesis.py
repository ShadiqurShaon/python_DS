def Find_is_valid(arr):
    arr = arr.replace(' ','')
    if arr=='':
        return True
    if len(arr)<2:
        return False
    paran = { '(':1,')':-1,'{':2,'}':-2,'[':3,']':-3 }
    stack = []
    index = 1
    stack.append(paran[arr[0]])
    while(len(arr)>index):
        if len(arr)-index<len(stack):
            return False
        key = arr[index]
        if paran[key]>0:
            stack.append(paran[arr[index]])
        elif paran[arr[index]]<0:
            if len(stack)==0:
                return False
            temp = stack.pop()
            if temp+paran[arr[index]]!=0:
                return False
        index+=1
    if len(stack)!=0:
        return False

    return True

print(Find_is_valid('((())'))
