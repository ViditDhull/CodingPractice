class Solution:
    def solve(self, N, arr):
        np = 0
        left_sum = 0
        right_sum = sum(arr)
        for i in range(N):
            right_sum = right_sum - arr[i]
            if left_sum == right_sum:
                np += 1
            left_sum += arr[i]
        return np

s1 = Solution()
#expected = 1 3 0
print(s1.solve(5, [3, -1, 0, 2, 0]), s1.solve(5, [2, -1, 0, 0, 1]), s1.solve(5, [ 1, 1, 1, 1, 2]))
