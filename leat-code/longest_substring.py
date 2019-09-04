def lengthOfLongestSubstring(self, s: str) -> int:
        
        dic = {}
        result = []
        final = 0
        print(s)
        for item in s:
            if item not in dic:
                dic[item] = item
                result.append(item)
            else:
                for idx, val in enumerate(result):
                    print(val)
                    
                    if val != item:
                        del result[idx]
                        
                    else:
                        del result[idx]
                        break
                        
                result.append(item)
                    
            if(len(result)>final):
                
                final = len(result)
            
            print(result)
            print(len(result))
        return final