# 590. N-ary Tree Postorder Traversal.py

# Given an n-ary tree, return the postorder traversal of its nodes' values.

# For example, given a 3-ary tree:

# Return its postorder traversal as: [5,6,3,2,4,1].

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""

class Solution(object):
	def __init__(self):
		self.res = []

	def helper(self, root):
		if root:
			for child in root.children:
				self.helper(child)
			self.res.append(root.val) 

	def postorder(self, root):
		self.helper(root)
		return self.res

