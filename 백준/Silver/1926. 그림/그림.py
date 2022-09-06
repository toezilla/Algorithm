from collections import deque

def bfs(x, y):
    global visited
    count = 1
    visited[y][x] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        now = queue.popleft()
        for i in range(4):
            xx = now[0] + dx[i]
            yy = now[1] + dy[i]
            if 0<=xx<m and 0<=yy<n:
                if grid[yy][xx] == 1 and visited[yy][xx] == 0:
                    queue.append((xx, yy))
                    visited[yy][xx] = 1
                    count += 1
    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    grid = []
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    number = 0
    max_width = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and visited[i][j] == 0:
                width = bfs(j, i)
                number+=1
                if width > max_width:
                    max_width = width

    print(number)
    print(max_width)
    