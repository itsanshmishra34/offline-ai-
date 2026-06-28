class Solution(object):
    def maxProfit(self, prices):
        a = prices[0]
        b = 0
        for i in prices:
            if i<a:
                a = i
            elif i-a>b:
                b = i-a
        return b

        