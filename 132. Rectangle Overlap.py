class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        r1_x1, r1_y1, r1_x2, r1_y2 = rec1
        r2_x1, r2_y1, r2_x2, r2_y2 = rec2

        if r1_x2 <= r2_x1 or r2_x2 <= r1_x1:
            return False

        if r1_y2 <= r2_y1 or r2_y2 <= r1_y1:
            return False
        
        return True