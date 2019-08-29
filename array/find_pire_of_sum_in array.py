array = [11,15,6,8,9,10]

def find_pire(array,key):
    dic = {}
    for item in array:
        dic[item] = item
    for item in array:
        if key - item in dic:
            return "Found"
    return "Not Found"

print(find_pire(array,16))