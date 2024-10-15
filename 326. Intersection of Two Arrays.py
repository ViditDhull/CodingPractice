class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count_dict1 = {}
        for i in nums1:
            if i in count_dict1:
                count_dict1[i] += 1
            count_dict1[i] = 1

        count_dict2 = {}
        for i in nums2:
            if i in count_dict2:
                count_dict2[i] += 1
            count_dict2[i] = 1
        
        result = []
        for i in count_dict2.keys():
            if i in count_dict1:
                for j in range(min(count_dict2[i], count_dict1[i])):
                    result.append(i)
        return result
