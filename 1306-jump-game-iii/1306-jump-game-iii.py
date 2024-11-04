class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        # targets = [i for i,j in enumerate(arr) if j ==0]
        # len_target = len(targets)
        
        n = len(arr)
        neighbors = deque([start])
        visited = set()
        result = []
        
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
        # print(visited)
        # if len(result)==len_target:
        #     return True
        return False

            
        
        
        
