class Solution(object):
    def recoverOrder(self, order, friends):
        """
        :type order: List[int]
        :type friends: List[int]
        :rtype: List[int]
        """
        a = []
        for i in order:
            if i in friends:
                a.append(i)
        return a

        