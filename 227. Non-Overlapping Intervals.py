class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]

        for start, end in intervals:
            if res[-1][1] <= start:
                res.append([start, end])
            else:
                if res[-1][1] > end:
                    res[-1] = ([start, end])
        return len(intervals) - len(res)