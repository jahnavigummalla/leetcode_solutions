class Solution:
    def subarraySum(self, nums, k):
        freq = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            if current_sum - k in freq:
                count += freq[current_sum - k]

            freq[current_sum] = freq.get(current_sum, 0) + 1

        return count  