# 884. Uncommon Words from Two Sentences.py

# 2019-11-24

# We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

# A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

# Return a list of all uncommon words. 

# You may return the list in any order.

# Example 1:

# Input: A = "this apple is sweet", B = "this apple is sour"
# Output: ["sweet","sour"]
# Example 2:

# Input: A = "apple apple", B = "banana"
# Output: ["banana"]
 

# Note:

# 0 <= A.length <= 200
# 0 <= B.length <= 200
# A and B both contain only spaces and lowercase letters.

import collections

class Solution(object):
	def uncommonFromSentences(self, A, B):
		"""
		:type A: str
		:type B: str
		:rtype: List[str]
		"""

		list_A = A.split(" ")
		list_B = B.split(" ")

		count_A = collections.Counter(list_A)
		count_B = collections.Counter(list_B)
		words = list((count_A.keys() | count_B.keys()) - (count_A.keys() & count_B.keys()))
		ans = []
		for word in words:
			if count_A[word] == 1 or count_B[word] == 1:
				ans.append(word)
		return ans

sol = Solution()

A = "this apple is sweet"
B = "this apple is sour"
# Output: ["sweet","sour"]

A = "apple apple"
B = "banana"
# Output: ["banana"]

res = sol.uncommonFromSentences(A,B)
print(res)     