import sys

def dfs(x, y):
    if x == n-1 and y == m-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    tmp = 0
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m and maze[yy][xx] < maze[y][x]:
            tmp += dfs(xx, yy)
    dp[y][x] = tmp

    return dp[y][x]


if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    
    m, n = map(int, input().split())
    maze = []
    for _ in range(m):
        maze.append(list(map(int, input().split())))

    dp = [[-1]*n for _ in range(m)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    print(dfs(0, 0))