class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        for i in range(len(nums)):
            a +=  min(nums[i] % 3, 3 - (nums[i] % 3))

        return a