def maxArea( height):
	i = 0
	j = len(height)-1
	result = 0
	while i<j:
		first = height[i]
		last = height[j]
		dis = j-i
		if first<=last:
			temp = first*dis
		else:
			temp = last*dis
		if temp>result:
			result = temp
		if first<=last:
			i+=1
		else:
			j-=1 
	return result
print(maxArea([1,8,6,2,5,4,8,3,7]))