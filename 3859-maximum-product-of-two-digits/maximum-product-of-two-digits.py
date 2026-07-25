class Solution(object):
    def maxProduct(self, n):
        a = sorted(str(n))
        return int(a[-1]) * int(a[-2])