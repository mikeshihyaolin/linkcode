# 703. Kth Largest Element in a Stream.py
# Design a class to find the kth largest element in a stream. 
# Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, 
# which contains initial elements from the stream. 
# For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

# Example:

# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# Note: 
# You may assume that nums' length ≥ k-1 and k ≥ 1.

import heapq
class KthLargest(object):

	def __init__(self, k, nums):
	    self.pool = nums
	    self.k = k
	    self.size = len(self.pool)
	    heapq.heapify(self.pool)
	    while self.size > k:
	    	heapq.heappop(self.pool)
	    	self.size -= 1
	    

	def add(self, val):
		if self.size < self.k:
			heapq.heappush(self.pool, val)
			self.size +=1
		elif val > self.pool[0]:
			heapq.heapreplace(self.pool, val)
		
		return self.pool[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


arr = [4,5,8,2]

sol = KthLargest(3, arr)


# res = sol.add(3)
# print(res)
print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))
