# 1134. Armstrong Number.py

# The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.

# Given a positive integer N, return true if and only if it is an Armstrong number.

 

# Example 1:

# Input: 153
# Output: true
# Explanation: 
# 153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.
# Example 2:

# Input: 123
# Output: false
# Explanation: 
# 123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.


class Solution(object):
	def isArmstrong(self, N):
		"""
		:type N: int
		:rtype: bool
		"""
		string = str(N)
		power_n = len(string)
		res = 0

		for s in string:
			res += int(s)**power_n

		if res == N:
			return True
		else:
			return False




sol = Solution()
Input = 153
Input = 123

res = sol.isArmstrong(Input)
print(res)



