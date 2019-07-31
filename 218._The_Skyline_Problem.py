# 218. The Skyline Problem.py

import heapq

class Solution(object):

	def getSkyline_mike(self, buildings):

		if buildings is None or len(buildings) == 0:
			return []

		scan_line = []

		# label start and end points
		for item in buildings:
		    scan_line.append((item[0], True, item[2]))
		    scan_line.append((item[1], False, item[2]))

		scan_line = sorted(scan_line, key=lambda v: (v[0], v[1], v[2]))

		height_max = 0 
		height_tmp = 0
		res = []
		hieght_heap = []

		print(scan_line)

		for i, arr in enumerate(scan_line):

			if i == 0:
				# initilization
				res.append([arr[0], arr[2]])
				height_max = arr[2]
				heapq.heappush(hieght_heap , -arr[2])

			else:
				if arr[1] == True:

					if arr[2] > height_max:
						res.append([arr[0], arr[2]])
						heapq.heappush(hieght_heap , -arr[2])				
				else:	
					if hieght_heap == []:
						heapq.heappush(hieght_heap , -arr[2])
						res.append([arr[0], height_max])
						# height_max = arr[2]

					else:
						height_tmp = -1*heapq.heappop(hieght_heap)

						if height_tmp > height_max:
							res.append([arr[0], height_max])
							# height_max = arr[2]

		return res


	def getSkyline(self, buildings):

	# Divide-and-conquer algorithm to solve skyline problem,
	# which is similar with the merge sort algorithm.

		n = len(buildings)
		# The base cases
		if n == 0:
			return []
		if n == 1:
			x_start, x_end, y = buildings[0]
			return [[x_start, y], [x_end, 0]] 
		
		# If there is more than one building, 
		# recursively divide the input into two subproblems.
		left_skyline = self.getSkyline(buildings[: n // 2])
		right_skyline = self.getSkyline(buildings[n // 2 :])

		# Merge the results of subproblem together.
		return self.merge_skylines(left_skyline, right_skyline)

	def merge_skylines(self, left, right):
	# Merge two skylines together.
		def update_output(x, y):
			# if skyline change is not vertical - 
			# add the new point
			if not output or output[-1][0] != x:
				output.append([x, y])
			# if skyline change is vertical - 
			# update the last point
			else:
				output[-1][1] = y

		def append_skyline(p, lst, n, y, curr_y):
			"""
			Append the rest of the skyline elements with indice (p, n)
			to the final output.
			"""
			while p < n: 
				x, y = lst[p]
				p += 1
				if curr_y != y:
					update_output(x, y)
					curr_y = y

		n_l, n_r = len(left), len(right)
		p_l = p_r = 0
		curr_y  = left_y = right_y = 0
		output = []

	# while we're in the region where both skylines are present
		while p_l < n_l and p_r < n_r:
		    point_l, point_r = left[p_l], right[p_r]
		    # pick up the smallest x
		    if point_l[0] < point_r[0]: 
		        x, left_y = point_l
		        p_l += 1
		    else: 
		        x, right_y = point_r 
		        p_r += 1
		    # max height (i.e. y) between both skylines
		    max_y = max(left_y, right_y)
		    # if there is a skyline change
		    if curr_y != max_y:
		        update_output(x, max_y)
		        curr_y = max_y

		# there is only left skyline
		append_skyline(p_l, left, n_l, left_y, curr_y)

		# there is only right skyline
		append_skyline(p_r, right, n_r, right_y, curr_y)

		return output

solution = Solution()

building_list = [ [2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8] ] 
building_list = [ [0, 1, 3] ] 
building_list = [[0,2,3],[2,5,3]]

building_list = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# expected output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
res = solution.getSkyline(building_list)
print(res)
