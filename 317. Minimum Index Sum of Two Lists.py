class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        sdict = {}
        for i in range(len(list1)):
            if list1[i] in list2:
                sdict[list1[i]] = i + list2.index(list1[i])
        least_sum = min(sdict.values())
        result = []
        for i in sdict.keys():
            if sdict[i] == least_sum:
                result.append(i)
        return result