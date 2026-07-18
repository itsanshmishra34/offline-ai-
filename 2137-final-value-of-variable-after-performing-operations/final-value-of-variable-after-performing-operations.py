class Solution(object):
    def finalValueAfterOperations(self, o):
        """
        :type operations: List[str]
        :rtype: int
        """
        a = 0
        for i in o:   
            if i=="--X" or i=="X--":
                a-=1
            else:
                a+=1
        return a    