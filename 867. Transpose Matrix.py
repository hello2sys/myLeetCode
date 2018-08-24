class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        m,n=len(A),len(A[0])
        B=[]
        for _ in range(n):
            B.append([0]*m)
        for i in range(n):
            for j in range(m):
                B[i][j]=A[j][i]
        return B
        

class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return list(zip(*A))        