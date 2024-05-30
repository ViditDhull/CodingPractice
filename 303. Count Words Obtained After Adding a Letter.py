class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        start = set([''.join(sorted(item)) for item in startWords])

        count = 0
        for item in targetWords:
            word = ''.join(sorted(item))
            n = len(item)
            for i in range(n):
                if word[:i] + word[i+1:] in start:
                    count += 1
                    break

        return count
