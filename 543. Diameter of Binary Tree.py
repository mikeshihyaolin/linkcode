# 543. Diameter of Binary Tree.py

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \     
#       4   5    
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.

# Definition for a binary tree node.
class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		

class Solution(object):

	def __init__(self):
		self.counter = 0
	
	def computer_diameter(self, root):
		if not root:
			return 0
		else:
			l_tree_c = self.computer_diameter(root.left)
			r_tree_c = self.computer_diameter(root.right)
			self.counter = max(self.counter, l_tree_c+r_tree_c)
			return max(l_tree_c,r_tree_c )+ 1

	def diameterOfBinaryTree(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		self.computer_diameter(root)
		return self.counter
		
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)


sol = Solution()
res = sol.diameterOfBinaryTree(root)
print(res)


