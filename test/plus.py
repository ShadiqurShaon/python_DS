def plus(arr):
    
    re = ''
    result = []
    for item in arr:
        re+=str(item)
    temp=int(re)+1
    for i in str(temp):
        result.append(int(i))
    return result

print(plus([9,9,9]))