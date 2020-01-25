# def lcs(str1,str2,m,n):
#    if m==0 or n==0:
#       return 0
#    elif str1[m-1]==str2[n-1]:
#       return 1+lcs(str1,str2,m-1,n-1)
#    else:
#       return max(lcs(str1,str2,m-1,n),lcs(str1,str2,m,n-1))

# print(lcs('aab','azb',3,3))
result = []
def alllcs(str1,str2,m,n,tempre):
   if m==0 or n==0:
         return []
   elif str1[m-1]==str2[n-1]:
      # tempre.append()
      return [str1[m-1]]+alllcs(str1,str2,m-1,n-1,tempre)
   else :
      return [alllcs(str1,str2,m-1,n,tempre),alllcs(str1,str2,m,n-1,tempre)]
      
  

print(alllcs('abc','bac',3,3,[]))
print(result)