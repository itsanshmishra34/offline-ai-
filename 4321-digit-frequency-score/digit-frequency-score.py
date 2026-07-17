class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        for i in str(n):
            sum += int(i)
        return sum
