# 200. Number of Islands.py

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
# You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3

class Node(object):

	def __init__(self):
		self.val 

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        






graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
  
  
row = len(graph) 
col = len(graph[0]) 
  
g = Graph(row, col, graph) 