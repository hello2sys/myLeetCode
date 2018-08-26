class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        def distance(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        n=len(points)
        ret=0
        for i in range(n):
            dist={}
            for j in range(n):
                D=distance(points[i],points[j])
                dist[D]=dist.get(D,0)+1
            for d in dist:
                ret+=dist[d]*(dist[d]-1)
        return ret