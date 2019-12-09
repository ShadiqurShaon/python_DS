def find(str_main,sub_str,start):
  if start==len(str_main):
    return 1 
  
  elif len(sub_str)==len(str_main):
    return 0

  len_sub = len(sub_str)
  main_sub = str_main[start:start+len_sub]
  if main_sub==sub_str:
    find(str_main,sub_str,start+len_sub)
  else:
    sub_str+=str_main[len(sub_str)]
    find(str_main,sub_str,0)

find('aaaabaaaa','a',0)

