class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        maxA = float("-inf")
        while i<len(height)-1:
            j=i+1
            while j<len(height):
                currA = min(height[i], height[j])*(j-i)
                if maxA < currA:
                    maxA = currA
                j+=1
            i+=1
        return maxA