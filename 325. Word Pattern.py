class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split()

        if len(pattern) != len(s_list):
            return False
        
        bi_dict = {}
        rev_dict = {}
        for i in range(len(s_list)):
            if pattern[i] in bi_dict:
                if bi_dict[pattern[i]] != s_list[i]:
                    return False
            else:
                bi_dict[pattern[i]] = s_list[i]

            if s_list[i] in rev_dict:
                if rev_dict[s_list[i]] != pattern[i]:
                    return False
            else:
                rev_dict[s_list[i]] = pattern[i]
        return True
