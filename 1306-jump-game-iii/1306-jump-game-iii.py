class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:        
        n = len(arr)
        neighbors = deque([start])
        visited = set()
        
        while len(neighbors)!=0:
            curr = neighbors.pop()
            if arr[curr] ==0:
                # result.append(curr)
                return True
            
            visited.add(curr)
            
            #check the new neighbors
            for i in [1,-1]:
                potential_neighbor = curr+i*arr[curr]
                if 0<=potential_neighbor<n and potential_neighbor not in visited:
                    neighbors.append(potential_neighbor)
        return False

            
        
        
        
