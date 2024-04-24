class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        at = {}
        for i in access_times:
            if i[0] not in at:
                at[i[0]] = [int(i[1])]
            else:
                at[i[0]].append(int(i[1]))
        def find_count(lst):
            lst.sort()
            lp, rp = 0, 1
            total_max = 1
            cur_max = 1
            while lp < len(lst) and rp < len(lst):
                if abs(lst[lp]-lst[rp]) < 100:
                    cur_max += 1
                    rp += 1
                else:
                    lp += 1
                    cur_max = 1
                    rp = lp + 1
                total_max = max(cur_max, total_max)
            return total_max
        res = []
        for i in at.keys():
            if find_count(at[i]) > 2:
                res.append(i)
        return res
