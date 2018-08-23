class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens=len(nums)
        if lens==1:
            return 1
        if lens==0:
            return 0
        first,second=0,1
        while second<lens:
            if nums[first]==nums[second]:
                second+=1
            else:
                first+=1
                nums[first],nums[second]=nums[second],nums[first]
                second+=1
        return first+1