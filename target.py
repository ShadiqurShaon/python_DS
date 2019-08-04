class calculator:
    def cal(self,array,target):
        holddict = {}
        for i,n in enumerate(array):
            holddict[n] = i+1
        for i,n in enumerate(array):
            if (target-n in holddict):
                return [i,holddict[n]]

if __name__=='__main__':
    newcal = calculator()
    array = [2, 7, 11, 15]
    print(newcal.cal(array,9))
