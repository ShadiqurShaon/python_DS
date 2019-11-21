def strStr( haystack, needle):
        if len(needle)==0:
            return 0
        if len(haystack)<len(needle):
            return -1
        h_index = 0
        n_index = 0
        while(h_index<len(haystack)):
            if haystack[h_index]==needle[n_index]:
                h_index+=1
                n_index+=1
            elif haystack[h_index]!=needle[n_index] and n_index>0:
                h_index = h_index-n_index+1
                n_index=0
            else:
                h_index+=1
                
            if len(needle)==n_index:
                return h_index-n_index
        return -1

print(strStr("ssssaa","saa"))