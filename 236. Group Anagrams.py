class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = []
        for i in range(len(strs)):
            each = {}
            for j in strs[i]:
                each[j] = 1 + each.get(j, 0)
            hm.append(each)
        res = []
        visited = {}
        for i in range(len(strs)):
            if i not in visited:
                combination = []
                combination.append(strs[i])
                visited[i] = 1
                for j in range(i+1, len(strs)):
                    if j not in visited:
                        if hm[i] == hm[j]:
                            combination.append(strs[j])
                            visited[j] = 1
                res.append(combination)
        return res