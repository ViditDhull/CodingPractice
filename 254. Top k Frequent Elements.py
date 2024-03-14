class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        res = [k for k, v in sorted(freq.items(), key = lambda item : item[1])]
        return res[::-1][:k]