def zikzak(string, col):
    st = string
    col = col-1
    # arr = ['0']*len(str)
    counter = 0
    flag = 0
    dict = {}
    for i in range(len(st)-1):
        print(str(st[i])+" "+(i)
        if flag==0:
            # print(counter)
            if counter not in dict:
                dict[counter] = []
                dict[counter].append(st[i])
            else:
                dict[counter].append(st[i])
            if(counter==col):
                flag=1
            else:
                counter+=1
        if flag==1:
            # print(counter)
            if counter not in dict:
                dict[counter] = []
                dict[counter].append(st[i])
            else:
                dict[counter].append(st[i])
            if counter==0:
                flag = 0
            else:
                counter-=1
    print(dict)
zikzak('PAYPALISHIRING',3)
