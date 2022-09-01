class Solution:
    def pacificAtlantic(self, A: List[List[int]]) -> List[List[int]]:
        def checkPacific(r, c, dpPacific, visP):
            if r>=len(A) or c>=len(A[0]):
                return False
            if r==0 or c==0:
                return True
            if dpPacific[r][c]:
                return dpPacific[r][c]
            if not dpPacific[r][c] and not visP[r-1][c] and A[r][c] >= A[r-1][c]:
                visP[r][c] = True
                dpPacific[r][c] = dpPacific[r][c] or checkPacific(r-1, c, dpPacific, visP)
            if not dpPacific[r][c] and not visP[r][c-1] and A[r][c] >= A[r][c-1]:
                visP[r][c] = True
                dpPacific[r][c] = dpPacific[r][c] or checkPacific(r, c-1, dpPacific, visP)
            if not dpPacific[r][c] and r+1 <= len(A)-1 and not visP[r+1][c] and A[r][c] >= A[r+1][c]:
                visP[r][c] = True
                dpPacific[r][c] = dpPacific[r][c] or checkPacific(r+1, c, dpPacific, visP)
            if not dpPacific[r][c] and c+1 <= len(A[0])-1 and not visP[r][c+1] and A[r][c] >= A[r][c+1]:
                visP[r][c] = True
                dpPacific[r][c] = dpPacific[r][c] or checkPacific(r, c+1, dpPacific, visP)
            else: 
                dpPacific[r][c] = dpPacific[r][c] or False
            visP[r][c] = False
            return dpPacific[r][c]
        
        def checkAtlantic(r, c, dpAtlantic, visA):
            if r<0 or c<0:
                return False
            if r==len(A)-1 or c==len(A[0])-1:
                return True
            if dpAtlantic[r][c]:
                return dpAtlantic[r][c]
            if not dpAtlantic[r][c] and not visA[r+1][c] and A[r][c] >= A[r+1][c]:
                visA[r][c] = True
                dpAtlantic[r][c] = dpAtlantic[r][c] or checkAtlantic(r+1, c, dpAtlantic, visA)
            if not dpAtlantic[r][c] and not visA[r][c+1] and A[r][c] >= A[r][c+1]:
                visA[r][c] = True
                dpAtlantic[r][c] = dpAtlantic[r][c] or checkAtlantic(r, c+1, dpAtlantic, visA)
            if not dpAtlantic[r][c] and r-1 >= 0 and not visA[r-1][c] and A[r][c] >= A[r-1][c]:
                visA[r][c] = True
                dpAtlantic[r][c] = dpAtlantic[r][c] or checkAtlantic(r-1, c, dpAtlantic, visA)
            if not dpAtlantic[r][c] and c-1 >= 0 and not visA[r][c-1] and A[r][c] >= A[r][c-1]:
                visA[r][c] = True
                dpAtlantic[r][c] = dpAtlantic[r][c] or checkAtlantic(r, c-1, dpAtlantic, visA)
            else: 
                dpAtlantic[r][c] = dpAtlantic[r][c] or False
            visA[r][c] = False
            return dpAtlantic[r][c]
        
        dpPacific = [[None for _ in range(len(A[0]))] for _ in range(len(A))]
        dpAtlantic = [[None for _ in range(len(A[0]))] for _ in range(len(A))]
        visP = [[False for _ in range(len(A[0]))] for _ in range(len(A))]
        visA = [[False for _ in range(len(A[0]))] for _ in range(len(A))]
        for i in range(len(dpPacific)):
            dpPacific[i][0] = True
            dpAtlantic[i][len(A[0])-1] = True
        for i in range(len(dpPacific[0])):
            dpPacific[0][i] = True
            dpAtlantic[len(A)-1][i] = True
        res = []
        for i in range(len(A)):
            for j in range(len(A[i])):
                if dpPacific[i][j] and dpAtlantic[i][j]:
                    res.append([i, j])
                    continue
                if checkPacific(i, j, dpPacific, visP) and checkAtlantic(i,j, dpAtlantic, visA):
                    res.append([i, j])
        return res