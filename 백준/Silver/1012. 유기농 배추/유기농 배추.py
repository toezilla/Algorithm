from collections import deque

def bfs(x, y):
    global visited
    Q = deque()
    Q.append((x, y))
    visited[y][x] = 1
    
    while Q:
        now = Q.popleft()
        for i in range(4):
            xx = now[0]+dx[i]
            yy = now[1]+dy[i]
            if 0<=xx<m and 0<=yy<n:
                if graph[yy][xx] == 1 and visited[yy][xx] == 0:
                    visited[yy][xx] = 1
                    Q.append((xx, yy))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m, n, k = map(int, input().split())
        graph = [[0]*m for _ in range(n)]
        visited = [[0]*m for _ in range(n)]
        cnt = 0
    
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
    
        for i in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
    
        for j in range(n):
            for i in range(m):
                if graph[j][i] == 1 and visited[j][i] == 0:
                    bfs(i, j)
                    cnt+=1
        print(cnt)