def hack(s,a):
    if a>s:
        return 0
    elif a==s:
        return 1
    else:
        return hack(s,a*10) or hack(s,a*20)
n=int(input())
for i in range(n):
    a=1
    s=int(input())
    r=hack(s,a)
    res="Yes" if r==1 else "No"
    print(res)  