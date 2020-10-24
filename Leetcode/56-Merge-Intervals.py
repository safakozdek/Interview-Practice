class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        res = []
        sortedIntervals = sorted(intervals, key=lambda x: x[0])

        start = sortedIntervals[0][0]
        end = sortedIntervals[0][1]
        for interval in sortedIntervals:
            if interval[0] > end:
                res.append([start, end])
                start = interval[0]
                end = interval[1]
            elif interval[1] > end:
                end = interval[1]

        res.append([start, end])
        return res
