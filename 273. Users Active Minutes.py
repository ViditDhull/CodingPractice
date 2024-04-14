class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d=dict()
        for i in logs:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]]=[i[1]]
        ans=[0]*k
        for val in d.values():
            ans[len(set(val))-1]+=1
        return ans