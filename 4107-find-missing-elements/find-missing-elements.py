class Solution(object):
    def findMissingElements(self, nums):
        a = []
        for i in range(min(nums),max(nums)):
            if i in nums:
                pass
            else:
                a.append(i)
        return a 
        