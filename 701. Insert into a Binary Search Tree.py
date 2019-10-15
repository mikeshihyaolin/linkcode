# 701. Insert into a Binary Search Tree.py

# Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

# Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

# For example, 

# Given the tree:
#         4
#        / \
#       2   7
#      / \
#     1   3
# And the value to insert: 5
# You can return this binary search tree:

#          4
#        /   \
#       2     7
#      / \   /
#     1   3 5
# This tree is also valid:

#          5
#        /   \
#       2     7
#      / \   
#     1   3
#          \
#           4

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def insertIntoBST(self, root, val):
		if not root:
			return TreeNode(val)
		else:
			self.function(root, val)

		return root

	def function(self, root, val):

		if root.val < val:
			if not root.right:
				root.right = TreeNode(val)
			else:
				self.function(root.right, val)
		else:
			if not root.left:
				root.left = TreeNode(val)
			else:
				self.function(root.left, val)




tree = TreeNode(4)
