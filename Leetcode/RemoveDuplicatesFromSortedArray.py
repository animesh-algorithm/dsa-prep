class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if i+1 < len(nums):
                if nums[i] == nums[i+1]:
                    nums.remove(nums[i])
                    continue
            i+=1