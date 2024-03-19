class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sn = mean * (n + len(rolls)) - sum(rolls)

        if sn < n or n * 6 < sn:
            return []

        res = []
        elementsToFill = n


        while elementsToFill > 0:
            newElement = sn // elementsToFill
            res.append(newElement)
            elementsToFill -= 1
            sn -= newElement

        return res