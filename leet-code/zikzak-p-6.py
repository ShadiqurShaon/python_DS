def zikzak(string, col):
    st = string
    col = col-1
    # arr = ['0']*len(str)
    counter = -1
    flag = 0
    dict = {}
    for i in range(len(st)):
        if flag==0:
            if(counter==col):
                flag=1
            else:
                counter+=1
            
        if flag==1:
            if counter==1:
                flag = 0
            counter-=1
        if counter not in dict:
            dict[counter] = []
            dict[counter].append(st[i])
        else:
            dict[counter].append(st[i])
    print(dict)
zikzak('PAYPALISHIRING',3)
