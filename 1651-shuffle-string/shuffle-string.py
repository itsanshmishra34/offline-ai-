class Solution(object):
    def restoreString(self, s, indices):
        res = [''] * len(s)
        
        for i in range(len(s)):
            res[indices[i]] = s[i]
        
        return ''.join(res)