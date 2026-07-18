class Solution(object):
    def minElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = []
        for i in nums:
            a=0
            for j in str(i):
                a+=int(j)
            b.append(a)
        return min(b)
