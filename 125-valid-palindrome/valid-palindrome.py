class Solution(object):
    def isPalindrome(self, s):
        text=""
        for i in s:
            if i.isalnum():
                text+=i.lower()
        return text==text[::-1]
            