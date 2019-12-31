def create(n):
    re = []
    for i in range(n):
        re.append([0]*n)
    i=0
    j=0
    fr=0
    lr=n-1
    fc=0
    lc=n-1
    for item in range(n*n):
        re[j][i]=item+1 
        if i!=lc and j==fr:
            i+=1
        elif i==lc and j!=lr:
            j+=1
        elif i<=lc and j==lr and i!=fc:
            i-=1
        elif i==fc and j<=lr and j!=fr:
            j-=1
        if i==fc and j==lr:
            fr+=1
            lc-=1
        elif i==fr and j==fc+1:
            lr-=1
            fc+=1
        


        
    for i in re:
        print(i,end='\n')

create(10)
