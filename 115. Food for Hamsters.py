class Solution(object):
    def minimumBuckets(self, hamsters):
        if 'HHH' in hamsters or hamsters[:2] == 'HH' or hamsters[-2:] == 'HH' or hamsters == 'H':
            return - 1
        else:
            return hamsters.count('H') - hamsters.count('H.H')