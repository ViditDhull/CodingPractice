class Solution(object):
    def minMovesToSeat(self, seats, students):
        moves = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            if seats[i] != students[i]:
                moves += abs(seats[i] - students[i])
        return moves