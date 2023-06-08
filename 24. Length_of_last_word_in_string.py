class Solution(object):
    def lengthOfLastWord(self, s):
        arr=s.strip().split( )
        return len(arr[-1])