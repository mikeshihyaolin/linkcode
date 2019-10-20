# 1119. Remove Vowels from a String.py
# 2019-10-19

# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

 

# Example 1:

# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# Example 2:

# Input: "aeiou"
# Output: ""
 

# Note:

# S consists of lowercase English letters only.
# 1 <= S.length <= 1000


class Solution(object):
	def removeVowels(self, S):
		"""
		:type S: str
		:rtype: str
		"""
		remove_list = ['a','e','i','o','u']
		res = ""

		for s in S:
			if s not in remove_list:
				res+=s
		return res



Input= "leetcodeisacommunityforcoders"
# Input= "aeiou"

sol = Solution()
res = sol.removeVowels(Input)

print(res)