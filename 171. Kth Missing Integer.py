class Solution(object):
    def findKthPositive(self, arr, k):
        if arr[0] != 1:
            if k > arr[0] - 1:
                k -= arr[0] - 1
            else:
                return k
        for i in range(1,len(arr)):
            if arr[i] - arr[i-1] > 1:
                if k >= arr[i] - arr[i-1]:
                    k -= arr[i] - arr[i-1] - 1
                else:
                    return arr[i-1] + k
        return arr[-1] + k