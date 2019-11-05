# 101. Symmetric Tree.py
# 2019-11-04

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3
 

# Note:
# Bonus points if you could solve it both recursively and iteratively.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

	def isMirror(self, l_tree, r_tree):
		if not l_tree and not r_tree:
			return True

		if not l_tree or not r_tree:
			return False

		return l_tree.val == r_tree.val and self.isMirror(l_tree.left, r_tree.right) and self.isMirror(l_tree.right, r_tree.left)

	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True

		return self.isMirror(root.left, root.right)


