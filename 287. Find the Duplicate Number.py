# 287. Find the Duplicate Number.py

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once

class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		dict = {}

		for s in nums:
			if s not in dict:
				dict[s] = 1
			else:
				dict[s] += 1
		
		# print(dict)
		dict = sorted(dict.items(), key = lambda x:x[1])
		# print(dict)
		# print(dict[-1][0])
		return dict[-1][0]


Input = [3,1,3,4,2]
Input = [1,3,4,2,2]
Input = [2,5,9,6,9,3,8,9,7,1]

sol = Solution()
res = sol.findDuplicate(Input)
print(res)
