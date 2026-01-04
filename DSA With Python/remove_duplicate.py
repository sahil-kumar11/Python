class solution:
    def remove_duplicate(arr,nums):
        if not nums:
            return 0 
        i=0
        for j in range(1,len(nums)):
            if nums[j] != nums[i]:
                i+=1
                nums[i] = nums[j]
        return i + 1
    
nums = [0,0,1,1,2,2,3,4,4]
sol = solution()
k = sol.remove_duplicate(nums)
print("Unique Array: ",k)
print("Array after removing duplicate:",nums[:k])