class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = k - 1
        vowels = ('a', 'e', 'i', 'o', 'u')
        count = 0
        n = len(s)
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_len = count
        while r < n - 1:
            if s[l] in vowels:
                count -= 1
            l += 1
            r += 1
            if s[r] in vowels:
                count += 1
            max_len = max(max_len, count)
        return max_len