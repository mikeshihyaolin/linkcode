# 50. Pow(x, n).py
# 2020-01-04

# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]

class Solution(object):
	def myPow(self, x, n):
		"""
		:type x: float
		:type n: int
		:rtype: float
		"""
		if x == 0:
			return 0

		res = 1	

		for i in range(abs(n)):
			print(i)
			res = res*x

		print(res)
		if n > 0:
			return res
		elif n == 0:
			return 1
		else:
			return 1/(res)


	# def myPow(self, x, n):
	# 	"""
	# 	:type x: float
	# 	:type n: int
	# 	:rtype: float
	# 	"""
	# 	if n == 0:
	# 		return 1
	# 	if n < 0:
	# 		x = 1 / x
	# 		n = -n
	# 	ans = 1
	# 	res = 1
	# 	while n:
	# 		if n % 2:
	# 		    ans *= x
	# 		n >>= 1
	# 		x *= x
	# 	return ans


x = 2.00000
n = 10

x = 2.10000
n = 3

x = 2.00000
n = -1

x = 0.00001
n = 2147483647

sol = Solution()
res = sol.myPow(x, n)
print(res)