class Solution(object):
    def sortSentence(self, s):
        dic = {}
        s = s.split(' ')
        for i in s:
            dic[i[-1]] = i[:-1]
        result = [''] * len(s)
        print(result)
        for i in dic.keys():
            result[int(i)-1] += dic[i]
        return ' '.join(result)