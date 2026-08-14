class Solution:
    def maximumLengthSubstring(self, s):
        d = {}
        l = ans = 0

        for r in range(len(s)):
            d[s[r]] = d.get(s[r], 0) + 1

            while d[s[r]] > 2:
                d[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans