class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        sum = 0
        for j in range(len(nums)//2):
            sum += min(nums[i], nums[i+1])
            i += 2
        return sum
