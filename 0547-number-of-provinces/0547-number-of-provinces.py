class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        n=len(isConnected)
        neighbors={node:[] for node in range(n)}
        
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]==1 and i!=j:
                    # edges.add((i,j)
                    neighbors[i].append(j)
                    neighbors[j].append(i)

        nb_provinces=0
        not_visited = [i for i in range(n)]
        
        def dfs(node:int):
            not_visited.remove(node)
            for neighbor in neighbors[node]:
                if neighbor in not_visited:
                    dfs(neighbor)
                    
        while len(not_visited)>=1:
            nb_provinces+=1
            dfs(not_visited[0])
        
        return nb_provinces
        
            