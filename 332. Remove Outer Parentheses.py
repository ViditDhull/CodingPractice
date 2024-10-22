class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        str = ''
        depth = 0
        for i in s:
            if depth == 0 and i == '(':
                depth += 1
            elif depth == 1 and i == ')':
                depth -= 1
            else:
                if i == '(':
                    str += i
                    depth += 1
                else:
                    str += i
                    depth -= 1
        return str
