class Solution(object):
    def getSneakyNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set()
        sneaky_numbers = []
        
        for num in nums:
            if num in seen:
                sneaky_numbers.append(num)
                if len(sneaky_numbers) == 2:
                    break
            else:
                seen.add(num)
                
        return sneaky_numbers
        