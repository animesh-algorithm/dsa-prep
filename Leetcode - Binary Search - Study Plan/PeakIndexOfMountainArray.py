class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def fun(s, e):
            if s < e:
                mid = s+(e-s)//2
                if arr[mid] < arr[mid+1]:
                    return fun(mid+1, e)
                if arr[mid] > arr[mid+1]:
                    return fun(s, mid)
                else:
                    return mid
            return s
        return fun(0, len(arr)-1)
