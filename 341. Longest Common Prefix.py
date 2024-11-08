class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        for i in strs:
            if i == strs[0]:
                continue
            j = 0
            cur_prefix = ''
            while j < len(longest_prefix) and j < len(i):
                if longest_prefix[j] == i[j]:
                    cur_prefix += i[j]
                    j += 1
                else:
                    break
            longest_prefix = cur_prefix
        return longest_prefix
