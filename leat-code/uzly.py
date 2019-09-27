def uzly(n,a,b,c):
  i=2
  counter = 1
  while(1):
    if (i%a==0 or i%b==0 or i%c==0) and counter==n:
      return i
    counter+=1
    i+=1
print(uzly(3,2,3,5))

    