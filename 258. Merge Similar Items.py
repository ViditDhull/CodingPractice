class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        dict1 = {}
        items1.extend(items2)
        for i,j in items1:
            dict1[i] = dict1.get(i, 0) + j
        res = []
        for i in sorted(dict1.keys()):
            res.append([i, dict1[i]])
        return res