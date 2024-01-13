class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        #we can perceive the key from room a to room b as an edge 
        
#         n = len(rooms)
#         open = set()

#         def dfs(i):
#             open.add(i)
#             for j in rooms[i]:
#                 if j not in open:
#                     dfs(j)
#         dfs(0)
#         return len(open) == n
    
        visited = []
        
        def dfs(room : int):
            # nonlocal visited, rooms, result
            visited.append(room)
            for neighbor in rooms[room]:
                if neighbor in visited:
                    continue
                dfs(neighbor)
        
        dfs(0)   
        return len(visited) == len(rooms)
        