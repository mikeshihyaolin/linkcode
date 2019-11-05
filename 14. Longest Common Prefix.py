# 14. Longest Common Prefix.py
# 2019-11-02

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if not strs:
			return ""
		min_len = len(min(strs, key=len))
		continue_len = 0
		while continue_len <= min_len:
			for i, _ in enumerate(strs):
				if i>0:
					if strs[i][0:continue_len]!=strs[i-1][0:continue_len]:
						return "".join(strs[i][0:continue_len-1])
			continue_len += 1

		return "".join(strs[i][0:continue_len-1])



sol = Solution()

Input= ["flower","flow","flight"]
Input= ["dog","racecar","car"]
Input = []

res = sol.longestCommonPrefix(Input)
print(res)
print(type(res))
