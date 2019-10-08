# 938. Range Sum of BST.py

# Given the root node of a binary search tree, 
# return the sum of values of all nodes with value between L and R (inclusive).

# The binary search tree is guaranteed to have unique values.

 

# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32
# Example 2:

# Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
# Output: 23

# Note:

# The number of nodes in the tree is at most 10000.
# The final answer is guaranteed to be less than 2^31.
class Node: 
    def __init__(self,key): 
        self.left = None
        self.right = None
        self.val = key 
  
# A utility function to insert a new node with the given key 
def insert(root,node): 
    if root is None: 
        root = node 
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
  
# A utility function to do inorder tree traversal 
def inorder(root): 
    if root: 
        inorder(root.left) 
        print(root.val) 
        inorder(root.right) 


# # Input: 
# nums = [10,5,15,3,7,18]
# L = 7
# R = 15
# # Output: 32


# Input: 
nums = [10,5,15,3,7,13,18,1,None,6]
L = 6
R = 10
# Output: 23

for i, num in enumerate(nums):
	# print(num)
	if i == 0:
		root = Node(num)
	else:
		if num:
			insert(root, Node(num))


class Solution(object):
    def rangeSumBST(self, root, L, R):

		if not root:
			return 0

		res = 0

		if L<=root.val <= R:
			res += res + root.val
			res += self.rangeSumBST(root.left, L, R)
			res += self.rangeSumBST(root.right, L, R)

		elif root.val < L:
			res += self.rangeSumBST(root.right, L, R)
		elif root.val > R:
			res += self.rangeSumBST(root.left, L, R)
		return res

solution = Solution()

res = solution.rangeSumBST(root, L, R)
print(res)