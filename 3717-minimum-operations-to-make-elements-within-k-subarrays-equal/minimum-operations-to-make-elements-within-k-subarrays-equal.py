class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # Coordinate compression
        vals = sorted(set(nums))
        m = len(vals)

        rank = {v: i + 1 for i, v in enumerate(vals)}

        # Fenwick Trees
        bit1 = [0] * (m + 1)
        bit2 = [0] * (m + 1)

        def update(i, delta, value):
            while i <= m:
                bit1[i] += delta
                bit2[i] += delta * value
                i += i & -i

        # Find kth smallest and prefix count/sum
        def kth(target):
            idx = 0
            cnt = 0
            sm = 0

            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= m and cnt + bit1[nxt] < target:
                    idx = nxt
                    cnt += bit1[nxt]
                    sm += bit2[nxt]

                step >>= 1

            return idx + 1, cnt, sm

        # Calculate cost of every window
        costs = []
        window_sum = 0

        for i in range(n):
            update(rank[nums[i]], 1, nums[i])
            window_sum += nums[i]

            if i >= x:
                v = nums[i - x]
                update(rank[v], -1, v)
                window_sum -= v

            if i >= x - 1:
                pos, cnt, sm = kth((x + 1) // 2)

                median = vals[pos - 1]

                cost = (
                    median * cnt - sm
                    + window_sum - sm
                    - median * (x - cnt)
                )

                costs.append(cost)

        # Dynamic Programming
        INF = float('inf')

        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]

                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]
