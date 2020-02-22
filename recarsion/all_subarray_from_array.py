def subarray(arr,strat,end,result):
    if end==len(arr):
        return result
    elif strat>end:
        return subarray(arr,0,end+1,result)
    else:
        print(arr[strat:end+1])
        tem = arr[strat:end+1]
        result.append(tem)
        return subarray(arr,strat+1,end,result)
    return result


def printSubsequences(arr, index, subarr): 
      
    # Print the subsequence when reach  
    # the leaf of recursion tree 
    if index == len(arr): 
          
        # Condition to avoid printing 
        # empty subsequence 
        if len(subarr) != 0: 
            print(subarr) 
      
    else: 
        # Subsequence without including  
        # the element at current index 
        printSubsequences(arr, index + 1, subarr) 
          
        # Subsequence including the element 
        # at current index 
        printSubsequences(arr, index + 1,subarr+[arr[index]]) 
      
    return


def subsequence(arr,index,subset):
    if len(arr)==index:
        print(subset)
        return

    subsequence(arr,index+1,subset)

    subsequence(arr,index+1,subset+[arr[index]])



def subarray1(arr,start,end):
    if start==len(arr):
        return
    if start>end:
        subarray1(arr,0,end+1)
    else:
        print(arr[start:end+1])
        subarray1(arr,start+1,end)
arr = [1, 2,3] 
subarray1(arr,0,0)
# printSubsequences(arr, 0, []) 
# arr = [1,2,3,4]
# print(subarray(arr,0,0,[]))