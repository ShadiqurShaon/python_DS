# def lcs(str1,str2,m,n):
#    if m==0 or n==0:
#       return 0
#    elif str1[m-1]==str2[n-1]:
#       return 1+lcs(str1,str2,m-1,n-1)
#    else:
#       return max(lcs(str1,str2,m-1,n),lcs(str1,str2,m,n-1))

# print(lcs('aab','azb',3,3))

def alllcs(str1,str2,m,n,tempre,result):
   if m==0 or n==0:
      result.append(tempre)
      # tempre = []
      return
   elif str1[m-1]==str2[n-1]:
      # tempre.append(str1[m-1])
      return alllcs(str1,str2,m-1,n-1,tempre+[str1[m-1]],result)
   else:
      return alllcs(str1,str2,m-1,n,tempre,result) or  alllcs(str1,str2,m,n-1,tempre,result)
  
   return result
print(alllcs('abc','bac',3,3,[],[]))
