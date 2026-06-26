class Solution(object):
    a = 0
    def concatWithReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.a = nums + nums[::-1]
        return self.a