class Solution:
    def minMaxDifference(self, num: int) -> int:
        sn = str(num)
        for i in sn:
            if i == '9':
                continue
            max_num = sn.replace(str(i), '9')
            break
        else:
            max_num = sn
        for i in sn:
            if i == '0':
                continue
            min_num = sn.replace(str(i), '0')
            break
        else:
            min_number = sn
        return int(max_num) - int(min_num)
