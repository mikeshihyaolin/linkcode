# 1189. Maximum Number of Balloons.py
# 2019-11-24

# Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return the maximum number of instances that can be formed.
 

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0

class Solution(object):
	def maxNumberOfBalloons(self, text):
		"""
		:type text: str
		:rtype: int
		"""
		target='balloon'
		ch_num=dict.fromkeys(target,0)

		for ch in text:
			if ch in target:
				ch_num[ch]+=1
		ch_num['l']=int(ch_num['l']/2)
		ch_num['o']=int(ch_num['o']/2)

		return min(ch_num.values())


sol = Solution()

text = "nlaebolko"
text = "loonbalxballpoon"
text = "leetcode"

res = sol.maxNumberOfBalloons(text)
print(res)