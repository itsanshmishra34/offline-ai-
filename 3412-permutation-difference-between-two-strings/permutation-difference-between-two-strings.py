class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        a = 0
        for i in s:
            a+=abs(s.index(i)-t.index(i))
        return a
