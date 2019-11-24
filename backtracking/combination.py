class solution:
  def __init__(self):
    self.result = []
  def getResult(self):
    return self.result
  def combo(self,arr,target,i,temp):
    if sum(temp)==target:
      sr = sorted(temp)
      if sr not in self.result:
        self.result.append(sr)
      return
    if sum(temp)>target:
      return 
    for i in range(i,len(arr)):
      self.combo(arr,target,i+1,temp+[arr[i]])
    return 

de = solution()

de.combo([2,5,2,1,2],5,0,[]) 
print(de.getResult())