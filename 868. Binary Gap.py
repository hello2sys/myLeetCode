class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_count,count=0,0
        while N:        
            if N%2==1: #第一个1
                N=N//2  #去掉这个1
                count=0
                while N:
                    if N%2==1:#找到后面的第一个1
                        count+=1
                        break
                    else: #否则继续找
                        N=N//2
                        count+=1
            else:
                N=N//2
            if count>max_count:
                max_count=count
        return max_count