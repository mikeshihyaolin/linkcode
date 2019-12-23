# 56. Merge Intervals.py
# 2019-12-19

# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

class Solution:
	def merge(self, intervals):
		intervals.sort(key = lambda x:x[0])
		length=len(intervals)
		res=[]
		for i in range(length):
			if res==[]:
				res.append(intervals[i])
			else:
				size=len(res)
				if res[size-1][0]<=intervals[i][0]<=res[size-1][1]:
					res[size-1][1]=max(intervals[i][1], res[size-1][1])
				else:
					res.append(intervals[i])
		return res


Input= [[2,6],[8,10],[15,18], [1,3]]
Input= [[1,4],[4,5]]

sol = Solution()
res = sol.merge(Input)
print(res)
