class Solution(object):
    def transformArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = []
        for i in nums:
            if i%2==0:
                a.append(0)
            else:
                a.append(1)
        return sorted(a)
        