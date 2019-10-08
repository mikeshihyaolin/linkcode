# 463. Island Perimeter.py

# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). 
# The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). 
# One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. 
# Determine the perimeter of the island.

class Solution(object):
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
	
		M, N = len(grid), len(grid[0])
		counts = 0
		neighbors = 0
		for i in range(M):
			for j in range(N):
				if grid[i][j] == 1:
				    counts += 1
				    if i < M - 1:
				        if grid[i + 1][j] == 1:
				            neighbors += 1
				    if j < N - 1:
				        if grid[i][j + 1] == 1:
				            neighbors += 1
		return 4 * counts - 2 * neighbors


# Input:
Input=[[0,1,0,0],
	   [1,1,1,0],
	   [0,1,0,0],
	   [1,1,0,0]]

# Output: 16

solution = Solution()
res = solution.islandPerimeter(Input)
print(res)