# 461. Hamming Distance.py

# The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

# Given two integers x and y, calculate the Hamming distance.


# Example:

# Input: x = 1, y = 4

# Output: 2


# The above arrows point to positions where the corresponding bits are different.

class Solution(object):
	
	# brute force
	def hammingDistance(self, x, y):
		res = 0

		bx = bin(x)[2:].zfill(32)
		by = bin(y)[2:].zfill(32)

		for i in range(32):
			if bx[i] !=by[i]:
				res += 1
		return res

	# XOR
	def hammingDistance(self, x, y):
		return bin(x^y).count('1')




solution = Solution()

x = 11
y = 4

res = solution.hammingDistance(x,y)
print(res)
