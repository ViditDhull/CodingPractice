class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        counts = Counter(reversed(s))
        max_count = max(counts.values())
        return "".join(char for char in reversed(counts) if counts[char] == max_count)
