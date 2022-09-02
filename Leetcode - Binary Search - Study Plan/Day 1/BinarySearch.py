class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def fun(s, e):
            if (s<=e):
                mid = s + (e-s)//2;
                if nums[mid]==target:
                    return mid
                if nums[mid]>target:
                    return fun(s, mid-1)
                else:
                    return fun(mid+1, e)
            return -1
        return fun(0, len(nums)-1)