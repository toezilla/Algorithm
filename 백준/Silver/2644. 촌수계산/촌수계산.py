from collections import deque

if __name__ == "__main__":
    n = int(input())
    start, end = map(int, input().split())

    graph = [[0]*(n+1) for _ in range(n+1)]
    m = int(input())
    for _ in range(m):
        x, y = map(int, input().split())
        graph[y][x] = 1
        graph[x][y] = 1

    visited = [[0]*(n+1) for _ in range(n+1)]


    Q = deque()
    Q.append((start, 0))
    while Q:
        now = Q.popleft()
        x = now[0]
        depth = now[1]
        if x == end:
            print(depth)
            break
        for i in range(n+1):
            if graph[x][i] == 1 and visited[x][i] == 0:
                visited[x][i] = 1
                visited[i][x] = 1
                Q.append((i, depth+1))
    else:
        print(-1)