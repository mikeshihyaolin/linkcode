# 20. Valid Parentheses.py
# 2019-10-26

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true


class Solution(object):
	def isValid(self, s):
		stack = []
		dict = {")":"(", "]":"[", "}":"{"}

		for ch in s:
			print(ch)
			if stack == []:
				stack.append(ch)
			else:
				if ch == "(" or ch == "[" or ch == "{":
					stack.append(ch)
				else:
					if [dict[ch]] == stack[:-2:-1]:
						stack.pop()
					else:
						return False
		return stack == []


Input = "()"
Input = "()[]{}"
Input = "(]"
Input = "([)]"
Input = "{[]}"
Input = "(])"

sol = Solution()
res = sol.isValid(Input)
print(res)

# abc = [1, 2,3,4,5]
# print(abc[:-2:-1])