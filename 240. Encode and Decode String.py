class Solution:
    def encode(self, strings):
        res = ''
        for i in strings:
            res += str(len(i)) + '#' + i
        
        return res
    
    def decode(self, string):
        res, i = [], 0
        while i < len(string):
            j = i
            while string[j] != '#':
                j += 1
            length = int(string[i : j])

            res.append(string[j + 1: j + 1 + length])
            i = j + 1 + length
        
        return res


#LeetCode Premium
string = ['#leet', '#code', 'love', 'you#']
s = Solution()
print(s.encode(string))
print(s.decode(s.encode(string)))