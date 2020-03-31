def find(strs):
    if len(strs)<1:
        return ''
    strs.sort(key=len)
    i=0
    tem_res = ''
    result = ''
    while(i<len(strs[0])):
        tem_res+=strs[0][i]
        counter = 0
        for item in strs:
            # if tem_res in item:
            #     counter+=1
            if len(item)>len(tem_res) and tem_res==item[:len(tem_res)]:
                counter+=1
        if counter==len(strs):
            result = tem_res
        i+=1
    print(result)
find(["ca","a"])
