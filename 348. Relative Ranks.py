class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rev_score = sorted(score, reverse = True)
        rank = {}
        for i in range(len(rev_score)):
            if i == 0:
                rank[rev_score[i]] = 'Gold Medal'
            elif i == 1:
                rank[rev_score[i]] = 'Silver Medal'
            elif i == 2:
                rank[rev_score[i]] = 'Bronze Medal'
            else:
                rank[rev_score[i]] = str(i + 1)
              
        res = []
        for i in range(len(score)):
            res.append(rank[score[i]])
        return res
