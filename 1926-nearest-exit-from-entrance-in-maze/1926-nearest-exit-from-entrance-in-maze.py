import copy
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m,n = len(maze), len(maze[0])
        start = tuple(entrance)
        q = deque([start])
        visited = set([start])
        res =0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                if (r,c) != start and (r==0 or c==0 or r==m-1 or c ==n-1):
                    return res

                for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                    row, col = r+i, c+j
                    if 0<=row<m and 0<=col<n and maze[row][col] =="." and (row,col) not in visited:
                        q.append((row,col))
                        visited.add((row,col))
            res+=1
        print(visited)
        print(q)
            
        print(q)
        print(visited)
        return -1
