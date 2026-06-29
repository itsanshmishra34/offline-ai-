class Solution(object):
    a=0
    def numOfStrings(self, patterns, word):
        for i in patterns:
            if i in word:
                self.a+=1
        return self.a
        