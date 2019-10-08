# 238. Product of Array Except Self.py

# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# Note: Please solve it without division and in O(n).

# Follow up:
# Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

class Solution(object):

	# #########################################
	# # approach 1: brute force
	# def productExceptSelf(self, nums):

	# 	res = []
	# 	for i, _ in enumerate(nums):
	# 		tmp = 1
	# 		for j, _ in enumerate(nums):
	# 			if j != i:
	# 				tmp = tmp *nums[j] 
	# 		res.append(tmp)

	# 	return res


	#########################################
	# approach 2
	# 	for i, _ in enumerate(nums):
	# 		if nums[i] == 0:
	# 			tmp = 1
	# 			for j, _ in enumerate(nums):
	# 				if i != j:
	# 					tmp = tmp * nums[j]
	# 			res.append(tmp)
	# 		else:
	# 			res.append(int(product_all/nums[i]))

	# 	return res

	#########################################
	# approach 3
	def productExceptSelf(self, nums):
		res = []
		l2r_scan = []
		r2l_scan = []

		for i, _ in enumerate(nums):
			if i == 0:
				l2r_scan.append(1)
			else:
				l2r_scan.append(l2r_scan[i-1]*nums[i-1])

		print(l2r_scan)

		for i, _ in enumerate(nums):
			if i == 0:
				r2l_scan.append(1)
			else:
				r2l_scan.append(r2l_scan[i-1]*nums[len(nums)-i])

		# print(r2l_scan)
		r2l_scan.reverse()
		print(r2l_scan)


		for i in range(len(nums)):
			res.append(r2l_scan[i]*l2r_scan[i])

		return res

nums = [4,5,1,8,2]


sol = Solution()

res = sol.productExceptSelf(nums)
print(res)