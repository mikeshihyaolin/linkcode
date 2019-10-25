# 31. Next Permutation.py

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.




Input = [1,2,3]

class Solution(object):
	def nextPermutation(self, nums):
		"""
		:type nums: List[int]
		:rtype: None Do not return anything, modify nums in-place instead.
		"""
		swapindex = -1
		n = len(nums)

		for i in range(n-2, -2, -1):
			if nums[i] < nums[i+1]:
				swapindex = i
				break
		if swapindex > -1:

			for i in range(n - 1, -1, -1):
				if nums[i] > nums[swapindex]:
					nums[i], nums[swapindex] = nums[swapindex], nums[i]
					break

		nums[swapindex+1:] = [nums[i] for i in range(n-1, swapindex, -1)]

		return nums


sol = Solution()
res = sol.nextPermutation(Input)
print(res)