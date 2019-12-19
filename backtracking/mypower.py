def myPow(x, n):
    if not n:
        return 1
    if n % 2:
        return x * myPow(x, n-1)
    return myPow(x*x, n/2)

print(myPow(2,5))