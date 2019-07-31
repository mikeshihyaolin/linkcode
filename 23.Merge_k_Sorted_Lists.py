# 23. Merge k Sorted Lists
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

# Example:

# Input:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# Output: 1->1->2->3->4->4->5->6

import heapq 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

	# # Approach 1: Brute Force
	# def mergeKLists_brute_force(self, lists):

	# 	self.nodes = []
	# 	head = point = ListNode(0)

	# 	for l in lists:
	# 		while l:
	# 			self.nodes.append(l.val)
	# 			l = l.next

	# 	for x in sorted(self.nodes):
	# 		point.next = ListNode(x)
	# 		point = point.next

	# 	return head.next

	# Approach 2: Compare one by one
	def mergeKLists_heapq(self, lists):

		self.nodes = []
		head = point = ListNode(0)

		q = []

		for l in lists:
			if l:
				heapq.heappush(q, (l.val, l))

		val, node = heapq.heappop(q)
		head.next = node
		point.next = node
		point = point.next 
		if node.next is not None:
			heapq.heappush(q, (node.next.val, node.next))

		while q:

			val, node = heapq.heappop(q)
			point.next = ListNode(val)
			point = point.next
			node = node.next
			if node:
				heapq.heappush(q, (node.val, node))
		return head.next


solution = Solution()


l1 = ListNode(1)
l1_2 = ListNode(4)
l1_3 = ListNode(5)
l1.next = l1_2
l1_2.next = l1_3

l2 = ListNode(1)
l2_2 = ListNode(3)
l2_3 = ListNode(4)
l2.next = l2_2
l2_2.next = l2_3

l3 = ListNode(2)
l3_2 = ListNode(6)
l3.next = l3_2


input_list = [l1, l2, l3]

res = solution.mergeKLists_heapq(input_list)

point = res

while point is not None:
	print(point.val)
	point = point.next

	



