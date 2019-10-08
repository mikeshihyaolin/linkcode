# 136. Single Number.py

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1

# Example 2:

# Input: [4,1,2,1,2]
# Output: 4

class Solution(object):
	def singleNumber(self, nums):
		dict = {}
		nums_length = len(nums)

		for i in range(nums_length):
			if nums[i] not in dict:
				dict[nums[i]] = 1
			else:
				dict[nums[i]] += 1

		single_num = min(dict.items(), key=lambda x:x[1])
		# print(single_num)
		# print(dict)

		if single_num[1] == 1:
			return single_num[0]


# nums = [2,2,1]
nums = [4,1,2,1,2]

sol = Solution()
res = sol.singleNumber(nums)
print(res)

