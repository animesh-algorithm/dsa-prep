class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        smaller, larger = 0, 0
        for num in nums:
            if num < target:
                smaller+=1
            elif num > target:
                larger+=1
        res = []
        for i in range(smaller, len(nums)-larger):
            res.append(i)            
        return res
            