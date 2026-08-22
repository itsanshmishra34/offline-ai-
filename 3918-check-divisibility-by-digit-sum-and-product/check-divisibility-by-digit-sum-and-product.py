class Solution(object):
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        b = 0
        a = 1
        for i in str(n):
            b+=int(i)
            a *= int(i)
        return n%(b+a)==0
        