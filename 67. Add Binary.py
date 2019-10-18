# 67. Add Binary.py

# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
	def addBinary(self, a, b):

		str_len = max(len(a), len(b)) + 1
		a = a.zfill(str_len)
		b = b.zfill(str_len)

		a = a[::-1]
		b = b[::-1]
		res = ""
		c = 0

		for i in range(str_len):

			tmp = int(a[i])+int(b[i])+c

			if tmp ==0:
				res += '0'
				c = 0
			elif tmp == 1:
				res += '1'
				c = 0
			elif tmp == 2:
				res+= '0'
				c = 1
			else:
				res += '1'
				c = 1
		
		res = res[::-1]

		if res[0]=="0":
			return str(res[1:])

		return str(res)


sol = Solution()

a = "11"
b = "1"
# a = "1010"
# b = "1011"

# a = "1010"
# b = "0011"

res = sol.addBinary(a,b)
print(res)