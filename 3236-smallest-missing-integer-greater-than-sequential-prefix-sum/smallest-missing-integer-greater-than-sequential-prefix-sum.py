class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                t+=nums[i]
            else:
                break
        while t in nums:
            t+=1
        return t