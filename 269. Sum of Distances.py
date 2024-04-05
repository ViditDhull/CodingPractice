class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num not in d:
                d[num] = []
            d[num].append(i)
        ans = [0] * len(nums)
        for num, val in d.items():
            suffixSum = sum(val)
            preffixSum = 0
            s = len(val)
            p = 0
            for i in val:
                preffixSum += i
                p += 1
                suffixSum -= i
                s -= 1
                ans[i] = -preffixSum + p * i - s * i + suffixSum
        return ans