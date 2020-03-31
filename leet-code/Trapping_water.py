def Rain_water(array):
    i=0
    stack = []
    # result = 0
    while i<len(array):
        # print(array[i])
        j=i+1
        stack.append(array[i])
        while j <len(array):
            if array[i]>=array[j]:
                stack.append(array[j])
            elif array[i]<array[j]:
                stack.append(array[j])
                break
            j+=1
        if len(stack)>2:
            print(stack.sort())
            stack = []
            i = j
        else:
            stack = []
            i = j
        

        # i+=1

# Rain_water([3,2,1,2,3])
Rain_water([0,1,0,2,1,0,1,3,2,1,2,1])