def Find_Deferance(arr):
  mi = min(arr)
  arr.sort()
  result = []
  sorted_array = arr
  print(sorted_array)
  min_absulate_def  = 100
  for i in range(len(sorted_array)-1):
    if sorted_array[i+1]-sorted_array[i]<min_absulate_def:
      min_absulate_def = sorted_array[i+1]-sorted_array[i]
  dic = {}
  for i in sorted_array:
    dic[i] = i
  for i in sorted_array:
    if i+min_absulate_def in dic:
      result.append([i,i+min_absulate_def])

  # result.sort()
      
  print(mi,min_absulate_def,result)


Find_Deferance([40,11,26,27,-20])