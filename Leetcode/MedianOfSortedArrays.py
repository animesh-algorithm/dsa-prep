class Solution:
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        total = len(nums1)+len(nums2)
        half = total//2
        l, r = 0, len(nums2)-1
        while True:
            i = (l+r)//2 #nums2
            j = half - i - 2 #nums1
            mid2 = nums2[i] if i >= 0 else float('-inf')
            adj2 = nums2[i+1] if (i+1) < len(nums2) else float('inf')
            mid1 = nums1[j] if j >= 0 else float('-inf')
            adj1 = nums1[j+1] if (j+1) < len(nums1) else float('inf')
            
            if mid1 <= adj2 and mid2 <= adj1:
                if total%2==0:
                    return (max(mid1, mid2) + min(adj1, adj2))/2
                return min(adj1, adj2)
            elif mid1 > adj2:
                l = i+1
            else:
                r = i-1
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i, j =0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
        while i < len(nums1):
            res.append(nums1[i])
            i+=1
        while j < len(nums2):
            res.append(nums2[j])
            j+=1
        mid = len(res)//2
        if len(res)%2==0:
            return (res[mid]+res[mid-1])/2
        return res[mid]