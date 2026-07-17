class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = str(n)
        return abs(n-int(a[::-1]))
        