class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:
            return []
        count=0
        i=0
        res = []
        originalLen = len(changed)//2
        changed.sort()
        while count!=originalLen and i<len(changed):
            if changed[i]*2 in changed[i+1:]:
                changed.remove(changed[i]*2)
                res.append(changed[i])
                count+=1
            i+=1
        return res if len(res) == originalLen else []