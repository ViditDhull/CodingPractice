class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        d1 = {}
        d2 = {}
        for i in nums1:
            d1[i] = 1
        for j in nums2:
            d2[j] = 1
        count1 = 0
        count2 = 0
        for i in range(len(nums1)):
            if nums1[i] in d2:
                count1 += 1
        for j in range(len(nums2)):
            if nums2[j] in d1:
                count2 += 1
        return [count1, count2]