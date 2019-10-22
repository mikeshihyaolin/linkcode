# 367. Valid Perfect Square.py

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 14
# Output: false

class Solution(object):
	def isPerfectSquare(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		left = 0
		right = num+1

		while  left < right:

			mid = int(right +left)/2
			# print(mid)

			if mid*mid == num:
				return True

			if mid*mid < num:
				left = mid + 1
			else:
				right = mid
		return False


	        
Input = 16
# Input = 14

sol = Solution()
res = sol.isPerfectSquare(Input)
print(res)