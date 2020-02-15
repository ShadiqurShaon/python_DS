def sumOfSerise(n):
    if n==1:
        return 1
    return (n**n)+sumOfSerise(n-1)


print(sumOfSerise(3))