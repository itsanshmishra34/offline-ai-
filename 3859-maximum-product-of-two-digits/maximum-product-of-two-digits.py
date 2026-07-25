class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        ans = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                ans = max(ans, digits[i] * digits[j])

        return ans