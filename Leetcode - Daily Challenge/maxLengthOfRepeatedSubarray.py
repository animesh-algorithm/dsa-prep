class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2) + 1) for _ in range(len(nums1) + 1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
        return max(max(row) for row in dp)
    
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def getAllSubarraysUsingRecursion(arr, n):
            subarrays = []
            for i in range(n):
                for j in range(i, n):
                    subarray = []
                    for k in range(i, j + 1):
                        subarray.append(arr[k])
                    subarrays.append(subarray)
            return subarrays
        if nums1 == nums2:
            return len(nums1)
        subarray1 = getAllSubarraysUsingRecursion(nums1, len(nums1))
        subarray2 = getAllSubarraysUsingRecursion(nums2, len(nums2))
        result = []
        for arr in subarray1:
            if arr in subarray2:
                result.append(len(arr))
        return max(result) if len(result) else 0