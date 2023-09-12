class Solution:
    def missingNumber(self,array,n):
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(array)
    
        missing_element = expected_sum - actual_sum
    
        return missing_element