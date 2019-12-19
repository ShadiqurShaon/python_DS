def permute(a,start,length):
    if start==length:
        print(a)
    else:
        for i in range(start,length+1):
            a[i],a[start]=a[start],a[i]
            permute(a,start+1,length)
            a[i],a[start]=a[start],a[i]

permute([1,2,3],0,2)