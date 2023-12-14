class Solution(object):
    def mergeArrays(self, nums1, nums2):
        rd = {}
        for i in nums1:
            rd[i[0]] = i[1]
        for j in nums2:
            if j[0] in rd:
                rd[j[0]] += j[1]
            else:
                rd[j[0]] = j[1]
        return sorted(rd.items())