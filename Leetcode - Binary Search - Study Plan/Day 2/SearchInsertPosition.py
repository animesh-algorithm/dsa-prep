class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def search(s, e):
            if s <= e:
                mid = s+(e-s)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] > target:
                    return search(s, mid-1)
                else:
                    return search(mid+1, e)
            return s
        return search(0, len(nums)-1)
