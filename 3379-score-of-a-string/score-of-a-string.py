class Solution(object):
    def scoreOfString(self, s):
        ansh = 0

        for i in range(1, len(s)):
            ansh += abs(ord(s[i]) - ord(s[i - 1]))

        return ansh