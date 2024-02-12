class Solution:
    def number_of_compnents(self, n, edges):
        if not n:
            return 0
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        count = 0
        visit = []

        def dfs(node):
            if node in visit:
                return False
            
            visit.append(node)
            for j in adj[node]:
                dfs(j)
            return True

        for i in range(n):
            if i in visit:
                continue
            
            if dfs(i):
                count += 1

        return count
    
sol = Solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(sol.number_of_compnents(n, edges))