class Solution:
    def reverseEqn(self, s):
        each_ele = []
        orig_arr = []
        for i in s:
            if i!='+' and i!='-' and i!='*' and i!='/':
                each_ele.append(i)
            else:
                orig_arr.append(''.join(each_ele))
                orig_arr.append(i)
                each_ele = []
        else:
            orig_arr.append(''.join(each_ele))
            
        rev_arr = [0] * (len(orig_arr))
        for i in range(len(orig_arr)):
            rev_arr[-i-1] = orig_arr[i]
        
        return ''.join(rev_arr)