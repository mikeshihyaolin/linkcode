# 49. Group Anagrams.py

# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.


class Solution(object):
	def char2code(self, strs):
		code = [0] * 26
		print(code)
		for char in strs:
			# print(char+" : "+ str(ord(char)-97))
			idx = ord(char)-97
			code[idx] += 1
		return str(code)

	def groupAnagrams(self, strs_list):

		dict = {}
		res = []

		for strs in strs_list:
			code = self.char2code(strs)

			if not code in dict:
				dict[code] = [strs]
			else:
				dict[code].append(strs)
		
		for code in dict.keys():
			res.append(dict[code])
		return res


sol = Solution()
Input= ["eat", "tea", "tan", "ate", "nat", "bat"]
res = sol.groupAnagrams(Input)

# print(res)