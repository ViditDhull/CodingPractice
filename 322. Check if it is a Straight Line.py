class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        xdiff = coordinates[0][0] - coordinates[1][0]
        ydiff = coordinates[0][1] - coordinates[1][1]
        if xdiff == 0:
            for i in range(len(coordinates) - 1):
                if coordinates[i][0] != coordinates[i+1][0]:
                    return False
            else:
                return True
        m = ydiff/xdiff
        c = coordinates[0][1] - (m * coordinates[0][0])
        for i in range(2, len(coordinates)):
            if coordinates[i][1] != m * coordinates[i][0] + c:
                return False
        return True
