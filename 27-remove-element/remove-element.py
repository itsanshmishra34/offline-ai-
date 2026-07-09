class Solution(object):
    def removeElement(self, nums, val):
        a = []
        for i in range(len(nums)):
            if nums[i]==val:
                pass
            else:
                a.append(nums[i])
        nums[:]=a
        return len(a)
        