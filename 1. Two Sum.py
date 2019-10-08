# 1. Two Sum.py
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].



class Solution(object):

	# # brute force
	# def twoSum(self, nums, target):
	# 	length = len(nums)
	# 	for i in range(length):
	# 		for j in range(i+1, length):
	# 			if nums[i]+nums[j] == target:
	# 				return [i, j]

	# hash-table
	def twoSum(self, nums, target):
		dict = {}
		length = len(nums)

		for i in range(length):
			complement = target - nums[i]
			if complement not in dict:
				dict[nums[i]] = i
			else:
				return [dict[complement], i]




nums = [2, 7, 11, 15]
target = 9

sol = Solution()
res = sol.twoSum(nums, target)
print(res)

