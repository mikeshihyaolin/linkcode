# 347. Top K Frequent Elements.py

# Given a non-empty array of integers, return the k most frequent elements.

# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# Note:


import heapq
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = collections.Counter(nums) 
        print(count)
        return heapq.nlargest(k, count.keys(), key=count.get) 
        # return heapq.nlargest(k, count) 
        
solution = Solution()

# Example 1:
# Input: 
nums = [1,1,1,2,2,3]
k = 2
# Output: [1,2]


# # Example 2:
# # Input: 
# nums = [1]
# k = 1
# # Output: [1]
# # Note:

nums = [1,1,1,2,2,3]
k = 2

res = solution.topKFrequent(nums, k)
print(res)