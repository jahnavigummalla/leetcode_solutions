from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # [left, right, weight, original index]
        arr = []
        for i, interval in enumerate(intervals):
            arr.append((interval[0], interval[1], interval[2], i))

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        ends = [x[1] for x in arr]

        # prev[i] = number of intervals before i
        # whose right endpoint is < arr[i].left
        prev = []

        for i in range(n):
            left = arr[i][0]
            j = bisect_left(ends, left, 0, i)
            prev.append(j)

        # dp[i][k] = best (score, indices)
        # using first i intervals and choosing at most k
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            left, right, weight, index = arr[i - 1]

            for k in range(1, 5):

                # Don't choose this interval
                option1 = dp[i - 1][k]

                # Choose this interval
                p = prev[i - 1]

                old_score, old_indices = dp[p][k - 1]

                option2_score = old_score + weight
                option2_indices = sorted(old_indices + [index])

                # Compare the two options
                if option2_score > option1[0]:
                    dp[i][k] = (option2_score, option2_indices)

                elif option2_score < option1[0]:
                    dp[i][k] = option1

                else:
                    # Same score -> lexicographically smaller
                    if option2_indices < option1[1]:
                        dp[i][k] = (option2_score, option2_indices)
                    else:
                        dp[i][k] = option1

        return dp[n][4][1]