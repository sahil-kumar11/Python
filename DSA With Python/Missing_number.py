class Solution:
    def Missing_number(self,a,N):
        total_sum = (N * (N+1)) // 2
        actual_sum = sum(a)
        return total_sum - actual_sum
a = [1,2,4,5]
N = 5
sol = Solution()
ans = sol.Missing_number(a,N)
print("Missing Number is:",ans)
