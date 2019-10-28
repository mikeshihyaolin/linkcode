# 297. Serialize and Deserialize Binary Tree.py

# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

# Example: 

# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5

# as "[1,2,3,null,null,4,5]"
# Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

# Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

class Codec:

	def __init__(self):
		self.vals = []
		self.dict = {}

	def pre_order(self, root):
		if not root:
			self.vals.append("N")

		else:
			self.vals.append(str(root.val))
			self.pre_order(root.left)
			self.pre_order(root.right)

	def in_order(self, root):
		if not root:
			self.vals.append("N")
		else:
			self.in_order(root.left)
			self.vals.append(str(root.val))
			self.in_order(root.right)

	def tree_build(self):

		if self.vals:
			val = self.vals.pop()
			if val == "N":
				return None
			root  = TreeNode(val)
			root.left = self.tree_build()
			root.right = self.tree_build()
			return root
		else:
			return None


	def serialize(self, root):
		"""Encodes a tree to a single string.

		:type root: TreeNode
		:rtype: str
		"""
		self.pre_order(root)
		print(self.vals)
		key = "".join(self.vals)
		self.dict[key] = self.vals

		return key

	def deserialize(self, data):
		"""Decodes your encoded data to tree.

		:type data: str
		:rtype: TreeNode
		"""
		self.vals = self.dict[data]


		self.vals = self.vals[::-1]

		tree_root = self.tree_build()

		return tree_root



sol = Codec()

serial = sol.serialize(root)
print(serial)

deserialize = sol.deserialize(serial)


# ------------

res = []



def preorder(root):
	if not root:
		res.append("N")
	else:
		res.append(root.val)
		preorder(root.left)
		preorder(root.right)

preorder(deserialize)
print(res)




