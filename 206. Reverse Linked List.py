# 206. Reverse Linked List.py

# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?


class LinkNode:
	def __init__(self, data):
		self.data = data
		self.next = None

class Single_Linklist:
	def __init__(self):
		self.head = None

	def traversal(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

class Solution(object):

	def __init__(self):
		self.head = None

	def traversal(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

	def reverseList(self):
		prev = None
		current = self.head

		while current is not None:

			next = current.next
			current.next = prev
			prev = current
			current = next

		self.head = prev




node_1 = LinkNode(1)
node_2 = LinkNode(2)
node_3 = LinkNode(3)

node_1.next = node_2
node_2.next = node_3

# linklist = Single_Linklist()
# linklist.head = node_1


# linklist.traversal()

linkedlist = Solution()
linkedlist.head = node_1

print(linkedlist.traversal())

linkedlist.reverseList()
print(linkedlist.traversal())



