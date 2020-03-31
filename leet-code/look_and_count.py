def Look_and_count (nums): 
    if nums==1:
        return '1'
    if nums==2:
        return '11'
    result = 11
    index=1
    while(index<nums-1):
        temp_result = str(result)
        re = ''
        counter = 1
        for i in range(len(temp_result)-1):
            if temp_result[i]==temp_result[i+1]:
                counter+=1
            else:
                re = re+str(counter)+str(temp_result[i])
                counter=1
        re = re+str(counter)+str(temp_result[i+1])
        print(re)
        result = re
        index+=1
    return result

print(Look_and_count(10))