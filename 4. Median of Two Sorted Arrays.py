# 4. Median of Two Sorted Arrays.py

# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


class Solution(object):

	# # 0. stupid solution
	# def findMedianSortedArrays(self, num1, num2):
	# 	num3 = num1 + num2

	# 	num3 = sorted(num3)

	# 	if len(num3)%2 == 1:
	# 		return num3[len(num3)/2]
	# 	else:
	# 		print(num3[int(len(num3)/2)-1])
	# 		print(num3[int(len(num3)/2)])

	# 		return (float(num3[int(len(num3)/2)])+float(num3[int(len(num3)/2)-1]))/2

	# 1. Recursive Approach
	# def getKth(self, A, B, k):
	# 	lenA = len(A); lenB = len(B)
	# 	if lenA > lenB: return self.getKth(B, A, k)
	# 	if lenA == 0: return B[k - 1]
	# 	if k == 1: return min(A[0], B[0])
	# 	pa = min(k/2, lenA); pb = k - pa
	# 	if A[pa - 1] <= B[pb - 1]:
	# 		return self.getKth(A[pa:], B, pb)
	# 	else:
	# 		return self.getKth(A, B[pb:], pa)

	# def findMedianSortedArrays(self, A, B):
	# 	lenA = len(A); lenB = len(B)
	# 	if (lenA + lenB) % 2 == 1: 
	# 	    return self.getKth(A, B, (lenA + lenB)/2 + 1)
	# 	else:
	# 	    return (self.getKth(A, B, (lenA + lenB)/2) + self.getKth(A, B, (lenA + lenB)/2 + 1)) * 0.5

	# def findMedianSortedArrays(self, num1, num2):

	# 	if len(num1) > len(num2):
	# 		return self.findMedianSortedArrays(num2, nums1)

	# 2. Bineary Search
	# def findkth()
	def findMedianSortedArrays(self, num1, num2):
		if len(num1) > len(num2):
			return self.findMedianSortedArrays(num2, num1)

		if len(num2) == 0:
			return None
		
		if len(num1) == 0:
			if len(num2)%2 == 1: 
				return num2[len(num2)/2]
			else:
				return (float(num2[len(num2)/2])+float(num2[len(num2)/2-1]))/2






solution = Solution()
nums1 = [1, 2, 3]
nums2 = [2]
# nums2 = []
# The median is 2.0


# nums1 = [1, 2]
# nums2 = [3, 4]
# # The median is (2 + 3)/2 = 2.5

res = solution.findMedianSortedArrays(nums1,nums2)
print(res)



