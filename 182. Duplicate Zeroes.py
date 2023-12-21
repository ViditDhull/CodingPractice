class Solution(object):
    def duplicateZeros(self, arr):
        i = 0
        lar = len(arr)
        while i < lar:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                i += 1
            i += 1
        while len(arr) > lar:
            arr.pop()