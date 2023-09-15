class Solution(object):
    def mergeTriplets(self, triplets, target):
        a, b, c = target
        maxi, maxj, maxk = 0, 0, 0

        for i, j, k in triplets:
            if i <= a and j <= b and k <= c:
                maxi = max(maxi, i)
                maxj = max(maxj, j)
                maxk = max(maxk, k)
                
        return maxi == a and maxj == b and maxk == c