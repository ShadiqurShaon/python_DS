result= []
def lcs(X, Y,temp, m, n): 
  
    if m == 0 or n == 0:
       result.append(temp) 
       return; 
    elif X[m-1] == Y[n-1]: 
       return lcs(X, Y,temp+[X[m-1]], m-1, n-1); 
    else: 
       return (lcs(X, Y,temp, m, n-1),lcs(X, Y,temp, m-1, n)) 
  
  
# Driver program to test the above function 
X = "abc"
Y = "bac"
lcs(X , Y,[], len(X), len(Y))
print(result)