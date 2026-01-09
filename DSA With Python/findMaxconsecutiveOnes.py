class Solution:
    def findMaxconsecutiveOnes(self,nums):
        maxi = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                count = 0
            maxi = max(maxi,count)
        return maxi

nums = [1,1,0,1,1,1,0,1,1]
sol = Solution()
ans = sol.findMaxconsecutiveOnes(nums)
print("The Number of Consecutive Ones are:",ans)