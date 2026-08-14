class Solution:
    def getFinalState(self, nums, k, m):
        for i in range(k):
            i = nums.index(min(nums))
            nums[i] *= m

        return nums