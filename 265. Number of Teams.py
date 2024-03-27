class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        nr = len(rating)
        up = [0] * nr
        down = [0] * nr
        for i in range(nr - 1, -1, -1):
            for j in range(i + 1, nr):
                if rating[i] < rating[j]:
                    up[i] += 1
                    teams += up[j]
                else:
                    down[i] += 1
                    teams += down[j]

        return teams