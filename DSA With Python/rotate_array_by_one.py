class solution:
    def rotate_array_by_one(self,nums):
        temp = nums[0]
        for i in range(1,len(nums)):
            nums[i-1] = nums[i]
        nums[-1] = temp

if __name__ == "__main__":
    sol = solution()
    nums = [1,2,3,4,5]
    sol.rotate_array_by_one(nums)
    print(nums)
