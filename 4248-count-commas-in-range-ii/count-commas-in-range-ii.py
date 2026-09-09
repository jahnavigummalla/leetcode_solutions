class Solution:
    def countCommas(self, n: int) -> int:
        total = 0
        start = 1000
        commas = 1
        while start <= n:
            end = min(n, start * 1000 - 1)
            total += (end - start + 1) * commas
            start *= 1000
            commas += 1
        return total