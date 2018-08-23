class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lens=len(nums)
        if lens==0:
            return 0
        if lens==1:
            return 1
        first,second,third=0,0,1
        while third<lens:
            if nums[second]==nums[third] and second-first+1<2:
                second+=1
                nums[second],nums[third]=nums[third],nums[second]
            elif nums[second]!=nums[third]:
                second+=1
                nums[second],nums[third]=nums[third],nums[second]
                first=second
            third+=1
        return second+1