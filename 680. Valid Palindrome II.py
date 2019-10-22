# 680. Valid Palindrome II.py
# 2019-10-19

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

# Example 1:
# Input: "aba"
# Output: True
# Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# Note:
# The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

class Solution(object):
	# def validPalindrome(self, s):
	# 	"""
	# 	:type s: str
	# 	:rtype: bool
	# 	"""

	# 	if s == s[::-1]:
	# 		return True

	# 	else:
	# 		for i, _ in enumerate(s):
	# 			if i == 0:
	# 				tmp = s[1:]
	# 				print(tmp)
	# 			else:
	# 				tmp = s[0:i]+s[i+1:]
	# 				print(tmp)

	# 			if tmp == tmp[::-1]:
	# 				return True
	# 		return False


	def isPalindrome(self, s):
		return s==s[::-1]

	def revised_str(self, s, start_p):
		return s[:start_p]+s[start_p+1:]

	def validPalindrome(self, s):
		left = 0
		right = len(s)-1

		if self.isPalindrome(s):
			return True

		else:
			while left < right:
				if s[left] != s[right]:
					print(self.revised_str(s, left))
					print(self.isPalindrome(self.revised_str(s, left)))
					print(self.revised_str(s, right))
					print(self.isPalindrome(self.revised_str(s, right)))
					print("----")
					return self.isPalindrome(self.revised_str(s, left)) or self.isPalindrome(self.revised_str(s, right))		
				left += 1
				right-= 1

			return True
		
Input= "aba"
Input= "abca"
Input= "abcddceba"
Input= "xabcddcba"

sol = Solution()
res = sol.validPalindrome(Input)
print(res)



