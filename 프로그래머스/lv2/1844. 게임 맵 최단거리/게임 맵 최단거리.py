from collections import deque

def bfs(x, y, maps):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    n = len(maps)
    m = len(maps[0])
    
    visited = [[0] * (m) for _ in range(n)]
    
    q = deque()
    q.append((x, y, 1))
    visited[y][x] = 1
    
    while q:
        cur_x, cur_y, cur_d = q.popleft()
        
        if cur_x == m-1 and cur_y == n-1:
            return cur_d
        
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]
            if 0<=next_x<m and 0<=next_y<n and not visited[next_y][next_x] and maps[next_y][next_x]:
                visited[next_y][next_x] = 1
                q.append((next_x, next_y, cur_d+1))
        
    return -1

def solution(maps):
    return bfs(0, 0, maps)
