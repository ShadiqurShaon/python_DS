def lengthOfLongestSubstring(s):
        
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
                    if val == item:
                        del result[0:idx+1]
                        break        
                result.append(item)
                    
            if(len(result)>final):
                
                final = len(result)
            
            print(result)
            # print(len(result))
        return final

print(lengthOfLongestSubstring('abacdcd'))
# print(lengthOfLongestSubstring('abcabcbcbb'))