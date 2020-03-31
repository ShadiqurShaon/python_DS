def int_to_roman(num):
    dic = {
        'I':1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90,
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000
    }

    result = 0
    i = 0
    print(len(num))
    if len(num)==1:
        result+=dic[num[0]]
    elif len(num)==2 and dic[num[i]]<dic[num[i+1]]:
         result+=dic[num[i]+num[i+1]]
    else:
        while i<len(num):
            if i<len(num)-1 and  dic[num[i]]<dic[num[i+1]]:
                result+=dic[num[i]+num[i+1]]
                # print(num[i])
                i+=2
            else:
                result+=dic[num[i]]
                i+=1
        # result+=dic[num[i]]
    print(result)
 
int_to_roman("MCMXCIV") 
        
        