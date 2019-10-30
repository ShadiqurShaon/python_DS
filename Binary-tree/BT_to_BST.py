
class newNode: 


	def __init__(self, data): 
		self.data = data 
		self.left = None
		self.right = None

def inorder(root):
  if root is None:
    return
  inorder(root.left)
  print(root.data,end='')
  inorder(root.right)

def binaryTreeToBST(root):
  s = set()
  inorder(root)

if __name__ == '__main__': 

	root = newNode(5) 
	root.left = newNode(7) 
	root.right = newNode(9) 
	root.right.left = newNode(10) 
	root.left.left = newNode(1) 
	root.left.right = newNode(6) 
	root.right.right = newNode(11) 

	""" Constructing tree given in 
		the above figure 
		5 
		/ \ 
		7	 9 
	/\ / \ 
	1 6 10 11 """

	# converting the above Binary tree to BST 
	binaryTreeToBST(root) 
	print("Inorder traversal of BST is: ") 
	inorder(root) 

# This code is contributed by 
# Shubham Singh(SHUBHAMSINGH10) 
