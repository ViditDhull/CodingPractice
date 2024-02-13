class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        
        visit = set()
        def dfs(node):
            if node in visit:
                return False

            visit.add(node)
            for i in range(n):
                if isConnected[node][i]:
                    if not dfs(i):
                        continue
                    visit.add(i)
                    dfs(i)
                
            return True

        count = 0
        for i in range(n):
            if i in visit:
                continue
            else:
                count += 1
                dfs(i)
        return count