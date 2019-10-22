# 426. Convert Binary Search Tree to Sorted Doubly Linked List.py

# Convert a BST to a sorted circular doubly-linked list in-place. Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.

# Let's take the following BST as an example, it may help you understand the problem better:


# We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# The figure below shows the circular doubly linked list for the BST above. The "head" symbol means the node it points to is the smallest element of the linked list.

 
# Specifically, we want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. We should return the pointer to the first element of the linked list.

# The figure below shows the transformed BST. The solid line indicates the successor relationship, while the dashed line means the predecessor relationship.

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.res = []
		self.dlist = Node(0)

	def inorder(self, root):
		if root:
			self.res = self.inorder(root.left)
			self.res.append(root.val)
			self.res = self.inorder(root.right)
		return self.res


	def treeToDoublyList(self, root):

		res = self.inorder(root)

		for i, _ in enumerate(res):
			if i == 0:
				self.dlist.val = res[0]
				self.dlist.left = Node(res[-1])
				tmp = self.dlist.left
				self.dlist.right = Node(res[i+1])
				self.dlist = self.dlist.right 
			else:
				self.dlist.val = res[i]
				self.dlist.left = tmp
				self.dlist.right = Node(res[i+1])
				self.dlist = self.dlist.right 
		return self.dlist





Tree = Node(4)
Tree.left = Node(2)
Tree.left.left = Node(1)
Tree.left.right = Node(3)
Tree.right = Node(5)


sol = Solution()
res = sol.inorder(Tree)

print(res)



