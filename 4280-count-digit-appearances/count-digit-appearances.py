class Solution(object):
    def countDigitOccurrences(self, nums, digit):
        """
        :type nums: List[int]
        :type digit: int
        :rtype: int
        """
        a = 0
        for i in nums:
            for j in str(i):
                if digit==int(j):
                    a+=1
        return a 
        