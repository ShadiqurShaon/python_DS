def add(arr,index):
    if index==len(arr):
        return 0
    if index%2==1:
        add1=arr[index]+add(arr,index+1)
    else:
        return add(arr,index+1)
    
    return add1
    

def mean(arr,sum1,index):

    if len(arr)==index:
        return sum1//(index-1)

    return mean(arr,sum1+arr[index],index+1)


def printSubArrays(arr,start,end):
    if end == len(arr): 
        return
      
    # Increment the end point and start from 0 
    elif start > end: 
        return printSubArrays(arr, 0, end + 1) 
          
    # Print the subarray and increment the starting 
    # point 
    else: 
        print(arr[start:end + 1]) 
        return printSubArrays(arr, start + 1, end) 
          
# Driver code 

def psubarray(arr,start,end):
    if end==len(arr):
        return
    
arr = [1, 2, 3,4] 
printSubArrays(arr, 0, 0) 
# print(mean([1, 2, 3, 4, 5],0,0))