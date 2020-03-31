
def segrate(arr):
  result={}
  final = []
  for item in arr:
    temp = "".join(sorted(item))
    if temp in result:
      result[temp].append(item)
    else:
      result[temp] = [item]
  for item in result.values():
    final.append(item)
  print(final)



arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
segrate(arr)