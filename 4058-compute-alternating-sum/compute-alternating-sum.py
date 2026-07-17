class Solution(object):
    def alternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in range(len(nums)):
            if i%2==0:
                a +=nums[i]
            else:
                a -=nums[i]
        return a