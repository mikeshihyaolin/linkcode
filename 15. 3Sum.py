# 15. 3Sum.py
# iven an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

class Solution(object):
	def threeSum(self, nums):
		nums.sort()
		res = []

		for i in range(len(nums)-2):

			if i > 0 and (nums[i]==nums[i-1]):
				continue

			j = i+1
			k = len(nums)-1

			while j < k:
				if  nums[i]+nums[j]+nums[k] == 0:
					res.append([nums[i], nums[j], nums[k]])

					while j < k and nums[j] == nums[j+1]:
						j += 1
					while j < k and nums[k] == nums[k-1]:
						k -= 1
					j +=1
					k -=1

				elif nums[j]+nums[k] + nums[i] < 0:
					j += 1
				else:
					k -= 1
		return res


nums = [-1, 0, 1, 2, -1, -4]
nums = [0,0,0,0]
solution = Solution()
res = solution.threeSum(nums)

print(res)




nums = [-1, 0, 1, 2, -1, -4]
sol = Solution()
res = sol.threeSum(nums)


