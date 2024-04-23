class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def bfs(start):
            queue = [start]
            seen = set()
            while queue:
                s = queue.pop(0)

                if s < 0: continue
                if s >= len(arr): continue
                if arr[s] == 0: return True

                if s in seen: continue
                seen.add(s)

                queue.append(s + arr[s])
                queue.append(s - arr[s])
            return False
        
        return bfs(start)