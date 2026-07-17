class Solution(object):
    def theMaximumAchievableX(self, num, t):
        """
        :type num: int
        :type t: int
        :rtype: int
        """
        for i in range(t):
            num+=2
        return num
        