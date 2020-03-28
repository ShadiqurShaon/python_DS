def make(s,numrow):

    pre_re = [[] for x in range(numrow)]
    string_index = 0
    row_index = 0
    counter = 0
    flag = True
    while(string_index<len(s)):
        
        pre_re[row_index].append(s[string_index])
        string_index+=1
        if counter==0:
            flag = True
        elif counter==numrow-1:
            flag =False
        
        if flag:
            row_index+=1
            counter+=1
        else:
            row_index-=1
            counter-=1
    result = ''
    for item in pre_re:
        result+=''.join(item)
    return result
print(make("PAYPALISHIRING",3))