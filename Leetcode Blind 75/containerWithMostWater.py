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
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=i+1
        maxA = float("-inf")
        while i<len(height)-1:
            if j==len(height):
                i+=1
                j=i+1
                continue
            currA = min(height[i], height[j])*(j-i)
            if maxA < currA:
                maxA = currA
            j+=1
        return maxA
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxA = float("-inf")
        while i<j:
            currA = min(height[i], height[j])*(j-i)
            maxA = max(maxA, currA)
            if height[i] > height[j]:
                j-=1
            else:
                i+=1
        return maxA