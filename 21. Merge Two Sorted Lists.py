# 21. Merge Two Sorted Lists.py

# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4

class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None


class Solution(object):

	def mergeTwoLists(self, l1, l2):

		if not l1 or not l2:
			return l1 or l2

		head = cur = ListNode(0)

		while l1 and l2:
			if l1.val < l2.val:
				cur.next = l1
				l1 = l1.next
			else:
				cur.next = l2
				l2 = l2.next
			
			cur = cur.next
			
		cur.next = l1 or l2

		return head.next





List1 = ListNode(1)
List1.next = ListNode(2)
List1.next.next = ListNode(4)

List2 = ListNode(1)
List2.next = ListNode(3)
List2.next.next = ListNode(4)

print(List1.val)
List1 = List1.next
print(List1.val)
List1 = List1.next
print(List1.val)

print(List2.val)
print(List2.next.val)
print(List2.next.next.val)

print("----")

sol = Solution()
res = sol.mergeTwoLists(List1, List1)

