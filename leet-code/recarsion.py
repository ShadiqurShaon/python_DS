class recarsion:
    def generate(self,rowNum,colNum):
        print(rowNum,colNum)
        if rowNum == 0 and colNum == 0 :
            return 
        if colNum != 0:
            return self.generate(rowNum,colNum-1)
        if rowNum != 0:
            return self.generate(rowNum-1,rowNum)
       
re = recarsion()
re.generate(5,5)