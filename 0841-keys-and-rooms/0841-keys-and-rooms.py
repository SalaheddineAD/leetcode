class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #we can perceive the key from room a to room b as an edge 
        
        visited = []
        result = 0
        
        def dfs(room : int):
            nonlocal visited, rooms, result
            result+=1
            visited.append(room)
            for neighbor in rooms[room]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        
        dfs(0)   
        return result == len(rooms)
        