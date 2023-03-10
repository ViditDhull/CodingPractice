class Compare:
    def at_least_two(self,nums):
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        else:
            return False