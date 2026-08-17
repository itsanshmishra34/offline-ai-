class Solution(object):
    def getMinDistance(self, nums, target, start):
        for i in range(len(nums)):
            if nums[i] == target:
                ans = abs(i - start)
                break

        for i in range(i + 1, len(nums)):
            if nums[i] == target:
                ans = min(ans, abs(i - start))

        return ans