class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        A=list(S)
        B=list(T)
        def f(A):
            lens=len(A)
            tmp=[]
            for i in range(lens):
                if A[i]!='#':
                    tmp.append(A[i])
                elif A[i]=='#' and len(tmp)!=0:
                    tmp.pop()
            return tmp
        A=f(A)
        B=f(B)
        return A==B