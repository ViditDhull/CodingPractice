class Solution:
    def valid_tree(self, n, adjacents):
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in adjacents:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = []
        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.append(node)
            for j in adj[node]:
                if j == prev:
                    continue

                if not dfs(j,node):
                    return False
            
            return True
        
        return dfs(0,-1) and n == len(visit)
    
sol = Solution()
n = 5
edges = [[0, 1], [0, 2], [0, 3], [1,4]]
print(sol.valid_tree(n, edges))