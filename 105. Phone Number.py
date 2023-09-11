class Solution(object):
    def letterCombinations(self, digits):
        n = len(digits)
        number_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if not digits or len(digits) < 1:
            return []
        res = []

        def backtracking(r):
            if len(r) == n:
                res.append(r)
            else:
                for i in number_map[digits[len(r)]]:
                    backtracking(r+i)
        backtracking('')
        return res