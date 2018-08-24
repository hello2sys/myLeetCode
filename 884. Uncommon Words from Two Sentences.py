class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ret=[]
        dic1={}
        dic2={}
        A=A.split(' ')
        B=B.split(' ')
        for a in A:
            dic1[a]=dic1.get(a,0)+1
        for b in B:
            dic2[b]=dic2.get(b,0)+1
        for b in B:
            if dic1.get(b,0)==0 and dic2[b]==1:
                ret.append(b)
        for a in A:
            if dic2.get(a,0)==0 and dic1[a]==1:
                ret.append(a)
        return ret