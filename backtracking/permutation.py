def prum(a,start,length):
    if start==length:
        print(a)
    else:
        for i in range(start,length+1):
            a[start],a[i]=a[i],a[start]
            prum(a,start+1,length)
           

prum([1,2,3],0,2)



# def permute(a, l, r): 
#     if l==r: 
#         print(a) 
#     else: 
#         for i in range(l,r+1): 
#             a[l], a[i] = a[i], a[l] 
#             permute(a, l+1, r) 
#             a[l], a[i] = a[i], a[l] # backtrack 
  
# # Driver program to test the above function 
# string = "ABC"
# n = len(string) 
# a = list(string) 
# permute(a, 0, n-1)  