class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m,n,ret=len(grid),len(grid[0]),0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ret+=4*grid[i][j]+2
                if i:
                    ret-=min(grid[i][j],grid[i-1][j])*2
                if j:
                    ret-=min(grid[i][j],grid[i][j-1])*2
        return ret