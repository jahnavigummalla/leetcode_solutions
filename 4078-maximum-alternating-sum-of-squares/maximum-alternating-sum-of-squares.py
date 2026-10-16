
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)

        total = 0
        n = len(nums)

        for i in range(n):
            if i < (n + 1) // 2:
                total += nums[n - 1 - i] ** 2
            else:
                total -= nums[n - 1 - i] ** 2

        return total
