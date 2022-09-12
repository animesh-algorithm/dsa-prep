class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                temp = nums[i]
                nums[i] = max(nums[i-1]+1, nums[i])
                count += nums[i]-temp
        return count
