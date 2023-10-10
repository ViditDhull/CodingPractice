class Solution(object):
    def minimumAbsDifference(self, arr):
        arr.sort()
        diff = 10000
        for i in range(len(arr) - 1):
            if (arr[i + 1] - arr[i]) < diff:
                diff = (arr[i + 1] - arr[i])
                output = []
                output.append([arr[i], arr[i+1]])
            elif (arr[i + 1] - arr[i]) == diff:
                output.append([arr[i], arr[i+1]])
        return output