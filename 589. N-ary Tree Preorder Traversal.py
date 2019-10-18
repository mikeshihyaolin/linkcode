# 589. N-ary Tree Preorder Traversal.py

# Given an n-ary tree, return the preorder traversal of its nodes' values.

# For example, given a 3-ary tree:


# Return its preorder traversal as: [1,3,5,6,2,4].



class Solution(object):

	def __init__(self):
		self.res = []

	def helper(self, root):
		if root:
			self.res.append(root.val)
			for child in root.children:
					self.helper(child)


	def preorder(self, root):
		"""
		:type root: Node
		:rtype: List[int]
		"""
		self.helper(root)
		return self.res





