# 1213. Intersection of Three Sorted Arrays.py

# Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, 
# return a sorted array of only the integers that appeared in all three arrays.

 
# Example 1:

# Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
# Output: [1,5]
# Explanation: Only 1 and 5 appeared in the three arrays.
 

# Constraints:

# 1 <= arr1.length, arr2.length, arr3.length <= 1000
# 1 <= arr1[i], arr2[i], arr3[i] <= 2000

import collections

class Solution(object):

	def convert(self,list):
		s = [str(i) for i in list]
		res = "".join(s)
		return res

	def arraysIntersection(self, arr1, arr2, arr3):
		res = []
		arr_all = arr1 + arr2 + arr3
		s = self.convert(arr1)
		dict = collections.Counter(arr_all)

		for item in dict.items():
			# print(item)
			if item[1] == 3:
				res.append(item[0])

		return res





arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

sol = Solution()
res = sol.arraysIntersection(arr1, arr2, arr3)

print(res)