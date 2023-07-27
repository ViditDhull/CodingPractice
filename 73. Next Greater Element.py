class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        map_ele = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                map_ele[stack.pop()] = num
            stack.append(num)
        for i in xrange(len(nums1)):
            nums1[i] = map_ele.get(nums1[i], -1)
        return nums1