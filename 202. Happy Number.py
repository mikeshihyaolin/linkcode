# 202. Happy Number.py

# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example: 

# Input: 19
# Output: true
# Explanation: 
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution(object):
    
	def findhappy(self,n, counter):
		res = 0
		string = str(n)

		for s in string:
			res += pow(int(s),2)

		if res == 1:
			return True
		elif res != 1 and counter<1000:
			counter +=1
			return self.findhappy(res,counter)
		else:
			return False

	def isHappy(self, n):
        
		counter = 0
		return self.findhappy(n, counter)
		


n = 19

sol = Solution()
print(sol.isHappy(n))
