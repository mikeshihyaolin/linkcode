# 507. Perfect Number.py

# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)

import math
class Solution(object):

	def findFactor(self, num):

		if num ==1:
			return False

		if num < 0:
			return False

		i = 2
		dict = {}

		sum = 1
		root = math.sqrt(num)

		while i < root:

			if num % i ==0:

				dict[int(num/i)] = 1
	
				if i in dict:
					break

				# res.append(i)
				# res.append(int(num/i))
				sum += i
				sum += int(num/i)

			i += 1

		return sum == num


	def checkPerfectNumber(self, num):
		"""
		:type num: int
		:rtype: bool
		"""
		return self.findFactor(num)


Input = 28
sol = Solution()
res = sol.checkPerfectNumber(Input)
print(res)