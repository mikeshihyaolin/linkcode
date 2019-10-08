# 179. Largest Number.py

# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:

# Input: [10,2]
# Output: "210"
# Example 2:

# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.

from functools import cmp_to_key

class Solution(object):
    def smaller(self,a,b):
        strA = str(a) + str(b)
        strB = str(b) + str(a)
        if strA > strB :
            return False
        else:
            return True

    def largestNumber(self, nums):
        resultStr = ""
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if self.smaller(nums[i],nums[j]):
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        # print(nums )
        for i in nums:
            resultStr = resultStr + str(i)
            # print(resultStr)
        if (resultStr[0]=='0'):
            return '0'
        return resultStr


# Input: [3,30,34,5,9]
# Output: "9534330"
nums = [3,30,34,5,9]

sol = Solution()

res = sol.largestNumber(nums)
print(res)
