class Solution:
    def numberOfPoints(self, nums):
        points = set()

        for start, end in nums:
            for i in range(start, end + 1):
                points.add(i)

        return len(points)