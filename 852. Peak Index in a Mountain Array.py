class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        Max,max_idx=-1,0
        for idx,num in enumerate(A):
            if num>Max:
                Max=num
                max_idx=idx
        return max_idx