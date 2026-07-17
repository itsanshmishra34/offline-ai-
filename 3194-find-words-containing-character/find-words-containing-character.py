class Solution(object):
    def findWordsContaining(self, words, x):
        b = []
        for i in range(len(words)):
            if x in words[i]:
                b.append(i)
        return b