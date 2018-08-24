class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N=len(grid[0])
        m=[[-1]*N,[-1]*N]
        ret=0
        for i in range(N):
            for j in range(N):
                if grid[i][j]!=0:
                    ret+=1
                if grid[i][j]>m[0][j]:
                    m[0][j]=grid[i][j] #每列的最大值
                if grid[i][j]>m[1][i]:
                    m[1][i]=grid[i][j] #每行的最大值
        ret+=sum(sum(l) for l in m)
        return ret