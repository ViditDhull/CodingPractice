class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        alp = 'abcdefghijklmnopqrstuvwxyz'
        fd = {}
        for i in licensePlate:
            if i.lower() in alp:
                if i.lower() in fd:
                    fd[i.lower()] += 1
                else:
                    fd[i.lower()] = 1
        print(fd)
        p = 0
        result = [True] * len(words)
        while p < len(words):
            for i in fd.keys():
                if i not in words[p]:
                    result[p] = False
                    break
                else:
                    if fd[i] > words[p].count(i):
                        result[p] = False
                        break
            p += 1
        sl = 9999
        index = 0
        for i in range(len(words)):
            if result[i] == True and sl > len(words[i]):
                sl = len(words[i])
                index = i
        print(result)
        return words[index]