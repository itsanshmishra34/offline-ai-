class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
    
        """
        a,s=0,0
        for i in range(n+1):
            if i%m==0:
                s +=i
            else:
                a +=i
        return a-s