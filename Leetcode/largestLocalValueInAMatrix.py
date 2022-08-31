class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def findMax(rl, cl, ru, cu):
            max = 0
            for r in range(rl, ru+1):
                for c in range(cl, cu+1):
                    if grid[r][c] > max:
                        max = grid[r][c]
            return max
        n = len(grid)
        maxLocal = [[0 for i in range(n-2)] for j in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                maxLocal[i][j] = findMax(i, j, i+2, j+2)
        return maxLocal