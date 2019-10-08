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

	# min-heap
	def minMeetingRooms_heap(self, intervals):

		# If there is no meeting to schedule then no room needs to be allocated.
		if not intervals:
		    return 0

		# The heap initialization
		free_rooms = []

		# Sort the meetings in increasing order of their start time.
		intervals.sort(key= lambda x: x[0])

		
		# Add the first meeting. We have to give a new room to the first meeting.
		heapq.heappush(free_rooms, intervals[0][1])

		# For all the remaining meeting rooms
		for i in intervals[1:]:

		    # If the room due to free up the earliest is free, assign that room to this meeting.
		    if free_rooms[0] <= i[0]:
		        heapq.heappop(free_rooms)

		    # If a new room is to be assigned, then also we add to the heap,
		    # If an old room is allocated, then also we have to add to the heap with updated end time.
		    heapq.heappush(free_rooms, i[1])

		# The size of the heap tells us the minimum rooms required for all the meetings.
		return len(free_rooms)

	# scan line 
	def minMeetingRooms_scanline(self, intervals):
		if intervals is None or len(intervals) == 0:
		    return 0

		tmp = []

		# label start and end points
		for inter in intervals:
		    tmp.append((inter[0], "start"))
		    tmp.append((inter[1], "end"))

		tmp = sorted(tmp, key=lambda v: (v[0], v[1]))
		print(tmp)

		n = 0
		max_num = 0
		for arr in tmp:
			
			# start point+1
			if arr[1] == "start":
			    n += 1
			# end point-1
			else:
			    n -= 1
			max_num = max(n, max_num)
		return max_num


solution = Solution()

print("scan-line")
res = solution.minMeetingRooms_scanline([[0, 30],[5, 10],[15, 20]])
print(res)
res = solution.minMeetingRooms_scanline([[7,10],[2,4]])
print(res)
res = solution.minMeetingRooms_scanline([[7,10],[2,4]])
print(res)

print("min-heap")
res = solution.minMeetingRooms_heap([[0, 30],[5, 10],[15, 20]])
print(res)
res = solution.minMeetingRooms_heap([[7,10],[2,4]])
print(res)
res = solution.minMeetingRooms_heap([[7,10],[2,4]])
print(res)


intervals = [[0, 30],[5, 10],[15, 20]]

for inter in intervals:
	print(inter)


