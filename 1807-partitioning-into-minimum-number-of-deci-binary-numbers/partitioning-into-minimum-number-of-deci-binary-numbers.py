class Solution(object):
    def minPartitions(self, n):
        a = []
        for i in str(n):
            a.append(i)
        return int(max(a))

        