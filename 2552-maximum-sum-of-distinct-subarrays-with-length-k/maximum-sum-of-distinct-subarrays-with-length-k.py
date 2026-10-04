class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        seen = set()
        total = 0
        ans = 0
        left = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                total -= nums[left]
                left += 1

            seen.add(nums[right])
            total += nums[right]

            if right - left + 1 == k:
                ans = max(ans, total)

                seen.remove(nums[left])
                total -= nums[left]
                left += 1

        return ans