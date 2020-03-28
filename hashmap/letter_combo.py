class solution:
  def combination(self,digit):
    dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
    temp_re = None
    for item in range(len(digit)):
      if item==0:
        temp_re = self.make(dic[digit[item]],dic[digit[item+1]])
      elif item>1:
        temp_re = self.make(temp_re,dic[digit[item]])
    return temp_re
  def make(self,arr1,arr2):
    result = []
    for i in arr1:
      for j in arr2:
        result.append(i+j)
    return result

sol = solution()
print(sol.combination('234'))




