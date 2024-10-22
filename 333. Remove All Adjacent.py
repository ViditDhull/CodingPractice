class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = ['']

        for i in s:
            if i == stack[-1]:
                stack.pop(-1)
            else:
                stack.append(i)

        return ''.join(stack)
