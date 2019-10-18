# 953. Verifying an Alien Dictionary.py

# In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

# Example 1:

# Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
# Output: true
# Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
# Example 2:

# Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
# Output: false
# Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
# Example 3:

# Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
# Output: false
# Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

# Note:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 20
# order.length == 26
# All characters in words[i] and order are english lowercase letters.


# --------------
# Mike's approach XD
# class Solution(object):
# 	def cmp(self, s1, s2, order):

# 		p1 = order.find(s1)
# 		p2 = order.find(s2)
# 		print(p1)
# 		print(p2)

# 		if p1 > p2:
# 			return 9
# 		elif p1 < p2:
# 			return 1
# 		else:
# 			return 0

	
# 	def isAlienSorted(self, words, order):
# 		"""
# 		:type words: List[str]
# 		:type order: str
# 		:rtype: bool
# 		"""

# 		len_tmp = []
# 		c = len(words)

# 		i = 0
# 		while i < 100:

# 			tmp = 0
# 			for j in range(c-1):

# 				if len(words[j]) >i and len(words[j+1])> i:

# 					s1 = words[j][i]
# 					s2 = words[j+1][i]

# 					# print(s1)
# 					# print(s2)

# 					ttmp = self.cmp(s1, s2, order)
# 					tmp += ttmp
# 					# print(ttmp)

# 					if ttmp == 9:
# 						return False

# 					if len(words[j]) > len(words[j+1]) and ttmp!=1:
# 						return False

# 			i +=1
			
# 			if tmp == c-1:
# 				return True



class Solution(object):

	def isAlienSorted(self, words, order):
		dict = {}

		for i, s in enumerate(order):
			dict[s] = i

		print(dict)
		ans = sorted(words, key=lambda x: [dict[c] for c in x])
		print(ans)

		if ans == words:
			return True
		else:
			return False


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"

# words = ["word","world","row"] 
# order = "worldabcefghijkmnpqstuvxyz"

# words = ["apple","app"]
# order = "abcdefghijklmnopqrstuvwxyz"


# words = ["kuvp","q"]
# order = "ngxlkthsjuoqcpavbfdermiywz"


sol = Solution()
res = sol.isAlienSorted(words, order)
print(res)

    