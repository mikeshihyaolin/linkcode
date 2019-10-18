# 125. Valid Palindrome.py

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false

class Solution(object):
	def isPalindrome(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		res = []

		for ch in s:
			if ord("A") <= ord(ch) and ord(ch) <= ord("Z"):
				ch = chr(ord(ch) - ord("A") + ord('a'))
				res.append(ch)
			elif ord("a") <= ord(ch) and ord(ch) <= ord("z"):
				res.append(ch)
			elif ord("0") <= ord(ch) and ord(ch) <= ord("9"):
				res.append(ch)

		print(res)
		print(res[::-1])
		return res == res[::-1]


sol = Solution()

Input= "A man, a plan, a canal: Panama"
# Input= "race a car"

Input = "0P"

res = sol.isPalindrome(Input)
print(res)