# 315. Count of Smaller Numbers After Self.py

# You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

# Example:

# Input: [5,2,6,1]
# Output: [2,1,1,0] 
# Explanation:
# To the right of 5 there are 2 smaller elements (2 and 1).
# To the right of 2 there is only 1 smaller element (1).
# To the right of 6 there is 1 smaller element (1).
# To the right of 1 there is 0 smaller element.


# def binary_search(arr, val, start, end): 
#     # we need to distinugish whether we should insert 
#     # before or after the left boundary. 
#     # imagine [0] is the last step of the binary search 
#     # and we need to decide where to insert -1 
#     if start == end: 
#         if arr[start] > val: 
#             return start 
#         else: 
#             return start+1
  
#     # this occurs if we are moving beyond left's boundary 
#     # meaning the left boundary is the least position to 
#     # find a number greater than val 
#     if start > end: 
#         return start 
  
#     mid = (start+end)/2
#     if arr[mid] < val: 
#         return binary_search(arr, val, mid+1, end) 
#     elif arr[mid] > val: 
#         return binary_search(arr, val, start, mid-1) 
#     else: 
#         return mid 

Input = [5,2,6,1]
res = []

for i in range(len(Input)):
    count = 0
    for j in range(i+1, len(Input)):

        if Input[i] > Input[j]:
            count = count + 1
    res.append(count)

print(res)



import bisect


class Solution(object):

    def countSmaller(self, nums):
        # fir, sec, res = [], [], []
        # for i in nums[::-1]:
        #     res += [bisect.bisect_left(fir,i) + bisect.bisect_left(sec,i)]
        #     bisect.insort_left(sec,i)
        #     if len(fir) < 4*len(sec):
        #         fir = sorted(fir+sec)
        #         sec = []

        fir, sec, res = [], [], []
        for i in nums[::-1]:
            res += [bisect.bisect_left(sec,i)]
            bisect.insort_left(sec,i)
        return res


# Input: [5,2,6,1]
# Output: [2,1,1,0] 
Input= [5,2,6,1]

solution = Solution()
res = solution.countSmaller(Input)

print(res)
