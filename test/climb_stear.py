def climbStairs1(nstr):
    new = nstr.split('/')
    print(new)
    result=[]
    for item in new:
        if item!='' and item!='.':
            if item=='..':
                result.pop()
            else:
                result.append(item)
    final_path = '/'
    if len(result)!=0:
        for item in result:
            final_path+=item+"/"
        return final_path[:-1]
    else:
        return final_path


print(climbStairs1('/../'))   