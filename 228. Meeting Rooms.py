class Solution:
    def meeting_rooms(self, intervals):
        if not intervals:
            return False
        intervals.sort(key = lambda i : i[0])
        endp = intervals[0][1]
        for start, end in intervals[1:]:
            if endp > end:
                return False
            endp = end
        return True

# LeetCode Premium
test_case = [(5, 10), (15, 20)]
s = Solution()
print(s.meeting_rooms(test_case))