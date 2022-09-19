import sys
from collections import deque

def bfs(x: int, y: int) -> int:
    global max_length
    visited = [[0]*m for _ in range(n)]
    queue = deque()
    queue.append((x, y, 0))
    visited[y][x] = 1
    
    while queue:
        now = queue.popleft()
        for i in range(4):
            now_x, now_y, path = now[0]+dx[i], now[1]+dy[i], now[2]
            if 0<=now_x<m and 0<=now_y<n:
                if not visited[now_y][now_x] and graph[now_y][now_x] == 'L':
                    queue.append((now_x, now_y, path+1))
                    visited[now_y][now_x] = 1
    return path


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = []
    for _ in range(n):
        graph.append(list(input()))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    max_length = -1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'L':
                if max_length < (local_max := bfs(j, i)):
                    max_length = local_max

    print(max_length)
