class Solution(object):
    def numDifferentIntegers(self, word):
        integers = set()
        buffer = ''
        for i in word:
            if i.isnumeric():
                buffer += i
            else:
                if len(buffer) > 0:
                    integers.add(int(buffer))
                    buffer = ''
        if len(buffer) > 0:
            integers.add(int(buffer))
        return len(integers)