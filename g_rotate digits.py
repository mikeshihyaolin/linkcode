# Given a number N, return true if and only if it is a confusing number, which satisfies the following condition:
# We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9, 8, 6 respectively. 
# When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid. 
# A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.


class Solution:

	def rotate_digits(self, N):
		

    # def confusingNumber(self, N: int) -> bool:
    def confusingNumber(self, N):
    	res = 0
		for digit in range(len(N)):
			if(check(digit))



solution.Solution()



# class Solution {
# public:
#     int rotatedDigits(int N) {
#         int res = 0;
#         for (int i = 1; i <= N; ++i) {
#             if (check(i)) ++res;
#         }
#         return res;
#     }
#     bool check(int k) {
#         string str = to_string(k);
#         bool flag = false;
#         for (char c : str) {
#             if (c == '3' || c == '4' || c == '7') return false;
#             if (c == '2' || c == '5' || c == '6' || c == '9') flag = true;;
#         }
#         return flag;
#     }
# };