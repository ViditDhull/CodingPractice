class Solution(object):
    def removeAnagrams(self, words):
        ans=[words[0]]
        for i in range(1,len(words)):
            if(sorted(words[i-1])!=sorted(words[i])):
                ans.append(words[i])
        
        return ans