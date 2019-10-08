# 1046. Last Stone Weight.py

# We have a collection of rocks, each rock has a positive integer weight.

# Each turn, we choose the two heaviest rocks and smash them together.  Suppose the stones have weights x and y with x <= y.  The result of this smash is:

# If x == y, both stones are totally destroyed;
# If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
# At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

 

# Example 1:

# Input: [2,7,4,1,8,1]
# Output: 1
# Explanation: 
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.

import heapq

class Solution(object):
	def lastStoneWeight(self, stones):
		"""
		:type stones: List[int]
		:rtype: int
		"""

		if not stones:
			return 0

		stones = map(lambda x: x*(-1), stones)
		
		stones = list(stones)
		print("original list:")
		print(stones)

		heapq.heapify(stones)
		print("build a min-heap:")
		print(stones)
		print("-------------")

		while len(stones)>1:
			print(stones)
			x = heapq.heappop(stones)
			print("pop x: "+str(x))
			if stones:
				y = heapq.heappop(stones)
				print("pop y: "+str(y))
				if x != y:
					diff = abs(x-y)*(-1)
					heapq.heappush(stones, diff)
		
		if stones:
			return stones[0]*(-1)
		else:
			return 0



# Input: 
input = [2,7,4,1,8,1]
# Output: 1

# input = []
# # # Output: 0

# input = [2,2]
# # Output: 0

solution = Solution()
res = solution.lastStoneWeight(input)
print(res)