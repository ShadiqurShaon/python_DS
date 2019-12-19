def multiply(str1,str2):
    str_to_int = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    int_to_str = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    len_str1 = len(str1)-1
    num1=0
    for i in str1:
        num1+=str_to_int[i]*(10**len_str1)
        len_str1-=1
    # print(num1)
    len_str2 = len(str2)-1
    num2=0
    for i in str2:
        num2+=str_to_int[i]*(10**len_str2)
        len_str2-=1
    # print(num2)
    result_int = num1*num2
    result_str = ''
    # print(result_str)
    while(result_int!=0):
        reminder = result_int%10
        result_str+=int_to_str[reminder]
        result_int-=reminder
        result_int = result_int/10
    result=''
    for i in result_str[::-1]:
        result+=i
    print(result)

multiply('0','0')
