class Solution(object):
    def checkIfPangram(self, sentence):
        count_a = dict()
        for i in 'abcdefghijklmnopqrstuvwxyz':
            count_a[i] = 0
        for i in sentence:
            count_a[i] += 1
        
        for i in count_a.values():
            if i < 1:
                return False
        return True