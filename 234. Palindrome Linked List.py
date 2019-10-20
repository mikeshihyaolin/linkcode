# 234. Palindrome Linked List.py
# 2019-10-19

# Given a singly linked list, determine if it is a palindrome.

# Example 1:

# Input: 1->2
# Output: false
# Example 2:

# Input: 1->2->2->1
# Output: true



class ListNode(object):
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution(object):
	# def isPalindrome(self, head):
	# 	"""
	# 	:type head: ListNode
	# 	:rtype: bool
	# 	"""
	# 	res = []
	# 	while head:
	# 		res.append(head.val)
	# 		head = head.next

	# 	return res == res [::-1]


	def reverse(self, head):
		new_head = None
		while head:
			current = head
			head = head.next
			current.next = new_head
			new_head = current
		return new_head

	# approach 1: time: O(n), space: O(1)
	def isPalindrome(self, head):

		slow = fast = head

		if not head or not head.next:
			return True

		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next.next

		slow = slow.next # slow pointer points to the second half of the list
		slow = self.reverse(slow)

		while slow:

			if head.val != slow.val:
				return False

			slow = slow.next
			head = head.next
		return True


sol = Solution()

# Example 1
head = ListNode(1)
head.next = ListNode(2)

# Example 2
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(5)

res = sol.isPalindrome(head)
print(res)