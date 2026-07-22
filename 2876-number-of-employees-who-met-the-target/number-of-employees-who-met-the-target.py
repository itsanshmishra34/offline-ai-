class Solution(object):
    def numberOfEmployeesWhoMetTarget(self, hours, target):
        """
        :type hours: List[int]
        :type target: int
        :rtype: int
        """
        a = 0
        for i in hours:
            if i>=target:
                a+=1
        return a