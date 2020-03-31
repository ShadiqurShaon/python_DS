class group:
  def __init__(self):
    self.sic={}
    self.flag = 0

  def find_permute(self,a,start,length,stri):
    if start==length:
      if ''.join(a) in self.sic:
        self.sic[''.join(a)].append(stri)
        self.flag = 1
    else:
      for i in range(start,length+1):
        a[i],a[start]=a[start],a[i]
        self.find_permute(a,start+1,length,stri)
        a[i],a[start]=a[start],a[i]
    
  def work(self):
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    for item in input:
      self.find_permute(list(item),0,2,item)
      if self.flag!=1:
        self.sic[item]=[item]
      self.flag = 0
    print(self.sic)


cl = group()
cl.work()