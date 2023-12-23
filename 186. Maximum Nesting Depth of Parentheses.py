class Solution(object):
    def maxDepth(self, s):
        max_dep = 0
        cd = 0
        for i in s:
            if i == '(':
                cd += 1
                if cd > max_dep:
                    max_dep = cd
            elif i == ')':
                cd -= 1
        return max_dep