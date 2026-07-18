class Solution(object):
    def finalValueAfterOperations(self, o):
        """
        :type operations: List[str]
        :rtype: int
        """
        a = 0
        for i in o:   
            if "--" in i:
                a-=1
            else:
                a+=1
        return a    