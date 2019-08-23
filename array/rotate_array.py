class job:
  def rotate(self,list,d):
    temp = []
    for i in range(0,d):
      temp.append(list[i])
    counter = 0
    for i in range(0,len(list)):
      if (i >= len(list)-d):
        list[i] = temp[counter]
        counter+=1
      else:
        list[i] = list[i+d]
    # for i in range(d,0):
    #   list[len(list)-i] = temp[i]
    
    return list
if __name__ == "__main__":
    arra = [1,2,3,4,5,6,7]
    job = job()
    newarr = job.rotate(arra,2)

    for item in newarr:
      print(item)







    