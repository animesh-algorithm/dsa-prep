class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        m = {
            True:1,
            False:0
        }
        for row in image:
            temp = [m[not cell] for cell in row[-1::-1]]
            result.append(temp)
        return result