# 295.Find Median from Data Stream

# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

# For example,
# [2,3,4], the median is 3

# [2,3], the median is (2 + 3) / 2 = 2.5

# Design a data structure that supports the following two operations:

# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
 

# Example:

# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2

# Follow up:

# If all integer numbers from the stream are between 0 and 100, how would you optimize it?
# If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

# import heapq
# listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]    
# heapq.heapify(listForTree)             # for a min heap
# heapq._heapify_max(listForTree)        # for a maxheap!!
# If you then want to pop elements, use:

# heapq.heappop(minheap)      # pop from minheap
# heapq._heappop_max(maxheap) # pop from maxheap

import heapq 

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.input_list = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.input_list.append(num)
        

    # two heaps
    def findMedian(self):
        """
        :rtype: float
        """
        print("input list: "+str(self.input_list))
        min_heap = []
        max_heap = []

        for item in self.input_list:
        	heapq.heappush(min_heap, item)
        	heapq.heappush(max_heap, item)

        # heapq.heapify(min_heap)
        # heapq._heapify_max(max_heap)


        for i in range(len(self.input_list)/2):
        	val_min = heapq.heappop(min_heap)
        	val_max = heapq.heappop(max_heap)

        	# print("------")
        	# print(val_min)
        	# print(val_max)
        	# print(len(min_heap))
        	# print(len(max_heap))
        	# print("------")
        	# if len(min_heap) == len(max_heap) :
		

		# print("------")
		# print(val_min)
		# print(val_max)
		# print(min_heap)
		# print(max_heap)
		return (float(val_max) + float(val_min))/2


solution = MedianFinder()
solution.addNum(0)
res = solution.findMedian()
solution.addNum(1)
solution.addNum(2)
solution.addNum(3)
res = solution.findMedian()
print(res)

solution.addNum(3)
solution.addNum(3)
res = solution.findMedian()
print(res)