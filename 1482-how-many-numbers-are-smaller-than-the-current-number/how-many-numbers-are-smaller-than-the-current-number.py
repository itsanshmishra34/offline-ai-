class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        b = 0
        for i in nums:
            for j in range(len(nums)):
                if i >nums[j]:
                    b+=1
            a.append(b)
            b = 0
        return a