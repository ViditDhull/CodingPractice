class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        run_sum = 0
        for i in range(len(arr)):
            run_sum += arr[i]
            if run_sum == i * (i+1)/2:
                res += 1
        return res
