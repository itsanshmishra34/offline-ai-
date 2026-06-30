class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        last_seen = {'a': -1, 'b': -1, 'c': -1}
        total_count = 0
        
        for i, char in enumerate(s):
            # Update the most recent index of the current character
            last_seen[char] = i
            
            # Find the minimum of the last seen indices
            min_index = min(last_seen['a'], last_seen['b'], last_seen['c'])
            
            # If all characters have been seen, add the number of valid substrings ending at i
            if min_index != -1:
                total_count += (min_index + 1)
                
        return total_count