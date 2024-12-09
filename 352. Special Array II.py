class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        n = len(nums)
    
        parity = [num % 2 for num in nums]
        
        non_special = [0] * n
        
        for i in range(1, n):
            non_special[i] = non_special[i - 1] + (parity[i] == parity[i - 1])
        
        answer = []
        
        for from_i, to_i in queries:
            if non_special[to_i] - non_special[from_i] > 0:
                answer.append(False)
            else:
                answer.append(True)
        
        return answer
