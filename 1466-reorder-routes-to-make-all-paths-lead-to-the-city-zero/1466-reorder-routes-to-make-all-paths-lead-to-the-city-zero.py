class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        
        edges = {(a,b) for a,b in connections }
        neighbors = {city : [] for city in range(n) }
        visited = set()
        result = 0
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        # we start from 0 and then check if its neighbors are connected to it, if not we add 1 if not. Then check dfs of each of those neighbors
        def dfs(city):
            nonlocal neighbors, visited, result, edges 
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    result+=1
                visited.add(city)
                dfs(neighbor)
            
        dfs(0)    
        
        return result