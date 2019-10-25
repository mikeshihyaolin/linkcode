# 941. Valid Mountain Array.py

# Given an array A of integers, return true if and only if it is a valid mountain array.

# Recall that A is a mountain array if and only if:

# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]

# Example 1:
# Input: [2,1]
# Output: false

# Example 2:
# Input: [3,5,5]
# Output: false

# Example 3:
# Input: [0,3,2,1]
# Output: true
 
# Note:
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 

Input= [2,1]
Output= False

Input= [3,5,5]
Output= False

Input= [0,3,2,1]
# Output: true

# class Solution(object):
# 	def validMountainArray(self, A):
# 		"""
# 		:type A: List[int]
# 		:rtype: bool
# 		"""
# 		flag1 = -1
# 		flag2 = -1

# 		for i in range(len(A)):
# 			if i > 0:
# 				if A[i] - A[i-1] > 0 and flag1 == -1:
# 					flag1 = 1

# 				if A[i] - A[i-1] < 0 and flag2 == -1:
# 					flag2 = 1

# 				if A[i] == A[i-1]:
# 					return False

# 		if flag1 == -1 and flag2 == -1:
# 			return False

# 		if flag1 * flag2 == 1: 
# 			return True
# 		return False

class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        N = len(A)
        if N < 3:
            return False
        i = 0
        while i < N - 1:
            if A[i] < A[i + 1]:
                i += 1
            else:
                break
        if i == 0 or i == N - 1: return False
        while i < N - 1:
            if A[i] > A[i + 1]:
                i += 1
            else:
                break
        return i == N - 1


sol = Solution()
res = sol.validMountainArray(Input)
print(res)
