class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(words) + 1)
        vowels = {}
        for i in ['a', 'e', 'i', 'o', 'u']:
            vowels[i] = 1
        for i in range(len(words)):
            prefix_sum[i+1] = prefix_sum[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix_sum[i+1] += 1
        
        result = []
        for x, y in queries:
            result.append(prefix_sum[y + 1] - prefix_sum[x])
        
        return result
