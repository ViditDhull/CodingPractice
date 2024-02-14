class Solution:
    def meeting_rooms(self, intervals):
        start = sorted([ i[0] for i in intervals])
        end = sorted([ i[1] for i in intervals])

        s, e = 0, 0
        mr = 0
        cm = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                cm += 1
            else:
                e += 1
                cm -= 1
            mr = max(mr, cm)
        return mr
    
s = Solution()
test_case = [(0, 30), (5, 10), (15, 20)]
print(s.meeting_rooms(test_case))