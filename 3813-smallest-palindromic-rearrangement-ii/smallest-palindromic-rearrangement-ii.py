from collections import Counter

def comb(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    ans = 1
    for i in range(1, r + 1):
        ans = ans * (n - r + i) // i
    return ans

class Solution(object):
    def smallestPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        freq = Counter(s)

        half = [0] * 26
        mid = ""
        total = 0

        for ch in sorted(freq):
            if freq[ch] % 2:
                mid = ch
            half[ord(ch) - 97] = freq[ch] // 2
            total += freq[ch] // 2

        LIMIT = k

        def countWays(cnt):
            ways = 1
            used = 0
            for c in cnt:
                if c:
                    ways *= comb(used + c, c)
                    if ways >= LIMIT:
                        return LIMIT
                    used += c
            return ways

        if countWays(half) < k:
            return ""

        left = []

        for _ in range(total):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = countWays(half)

                if ways >= k:
                    left.append(chr(i + 97))
                    break
                else:
                    k -= ways
                    half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]