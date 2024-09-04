class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        i = 1
        n = 1
        while candies > 0 :
            if n < candies:
                candies -= n
                result[i - 1] += n
            else:
                result[i-1] += candies
                candies = 0
            if i == num_people:
                i = 1
            else:
                i += 1
            n += 1
                
        return result
