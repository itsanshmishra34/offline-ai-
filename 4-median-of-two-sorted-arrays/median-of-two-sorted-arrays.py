class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        s = sorted(nums1+nums2)
        n = len(s)
        mid = n // 2
        if n % 2 == 0:
            return (s[mid - 1] + s[mid]) / 2.0
        else:
            return s[mid]   