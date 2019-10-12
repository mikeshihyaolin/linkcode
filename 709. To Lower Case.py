# 709. To Lower Case.py

# Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

# Example 1:

# Input: "Hello"
# Output: "hello"
# Example 2:

# Input: "here"
# Output: "here"
# Example 3:

# Input: "LOVELY"
# Output: "lovely"

class Solution(object):
	def toLowerCase(self, str):
		res = ''
		
		for s in str:
			if ord(s) >= ord('A') and ord(s) <= ord('Z'):
				ch = chr(ord(s)-ord('A')+ord('a'))
				res +=ch			
			else:
				res += s
		return res


# Input= "Hello"
Input= "here"
Input= "LOVELY"


sol = Solution()
results = sol.toLowerCase(Input)
print(results)


