
# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
# find the minimum number of conference rooms required.

# # Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2

# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

import heapq 

class Solution:

	# scan line 扫描线
	def minMeetingRooms_scanline(self, intervals):
	    if intervals is None or len(intervals) == 0:
	        return 0

	    tmp = []

	    # 标记起始点终止点
	    for inter in intervals:
	        tmp.append((inter[0], True))
	        tmp.append((inter[1], False))

	    # 排序
	    tmp = sorted(tmp, key=lambda v: (v[0], v[1]))

	    n = 0
	    max_num = 0
	    for arr in tmp:
	        # 起始点+1
	        if arr[1]:
	            n += 1
	        # 终止点-1
	        else:
	            n -= 1
	        max_num = max(n, max_num)
	    return max_num

    # min-heap
	def minMeetingRooms_heap(self, intervals):

		if intervals is None or len(intervals) == 0:
			return 0

		arr_start = []
		arr_end = []

		# build a start-array  
		for inter in intervals:
			arr_start.append((inter[0], inter[1]))

		# sort by start points
		arr_start = sorted(arr_start, key=lambda v: (v[0]))


		arr_end = [arr_start[0][1]]
		# build a end-heap
		heapq.heapify(arr_end) 
        

		for i in range(1, len(arr_start)): 
			current_meeting = arr_start[i]
			earliest = heapq.heappop(arr_end)

			if (current_meeting[0] >= earliest):
				earliest = current_meeting[0]
			else:
				heapq.heappush(arr_end,current_meeting[1]) 


			heapq.heappush(arr_end, earliest)

		return len(arr_end)



solution = Solution()

print("scan-line")
res = solution.minMeetingRooms_scanline([[0, 30],[5, 10],[15, 20]])
print(res)
res = solution.minMeetingRooms_scanline([[7,10],[2,4]])
print(res)

print("min-heap")
res = solution.minMeetingRooms_heap([[0, 30],[5, 10],[15, 20]])
print(res)
res = solution.minMeetingRooms_heap([[7,10],[2,4]])
print(res)

