class Solution(object):
    def decodeMessage(self, key, message):
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        conv = {}
        index = 0
        for i in key:
            if i not in conv and i != ' ':
                conv[i] = alphabets[index]
                index += 1
        decoded = ''
        for i in message:
            if i == ' ':
                decoded += i
            else:
                decoded += conv[i]
        return decoded