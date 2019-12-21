def combo(num1,num2):

  if num1=='' and num2!='':
    return num2
  if num2=='' and num1!='':
      return num1
  
  str1 = num1
  str2 = num2
  
  str_to_int = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
  int_to_str = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}


  len_str1 = len(str1)-1
  if len_str1>0:
      
      num1=0
      for i in str1:
          num1+=str_to_int[i]*(10**len_str1)
          len_str1-=1
      # print(num1)
  else:
      num1 = str_to_int[str1]
  len_str2 = len(str2)-1
  # if len_str2>0:
  #     num2=0
  #     for i in str2:
  #         num2+=str_to_int[i]*(10**len_str2)
  #         len_str2-=1
  # else:
  #     num2 = str_to_int[str2]
  # print(num2)
  temp_re = 0
  for i in str2:
    tem = (str_to_int[i]*(10**len_str2))
    temp_re=temp_re+(num1*tem)
    len_str2-=1
  return temp_re
  # result_int = num1*num2
  # if result_int!=0:
      
  #     result_str = ''
  #     while(result_int!=0):
  #         reminder = result_int%10
  #         result_str+=int_to_str[reminder]
  #         result_int-=reminder
  #         result_int = result_int/10
  #     result=''
  #     for i in result_str[::-1]:
  #         result+=i
  # else:
  #     result = '0'
  # return result


print(combo('12','12'))
