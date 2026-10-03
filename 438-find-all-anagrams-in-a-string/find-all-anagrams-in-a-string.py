class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []

        result = []

        p_count = {}
        window_count = {}

        for ch in p:
            p_count[ch] = p_count.get(ch, 0) + 1

        left = 0

        for right in range(len(s)):
            ch = s[right]
            window_count[ch] = window_count.get(ch, 0) + 1

            if right - left + 1 > len(p):
                left_ch = s[left]
                window_count[left_ch] -= 1

                if window_count[left_ch] == 0:
                    del window_count[left_ch]

                left += 1

            if window_count == p_count:
                result.append(left)

        return result