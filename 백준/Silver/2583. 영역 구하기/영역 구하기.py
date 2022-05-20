import sys
sys.setrecursionlimit(10**5)

def dfs(depth, x, y):
    board[y][x] = 1
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m and board[yy][xx]==0:
            depth = dfs(depth+1, xx, yy)
    return depth



if __name__ =="__main__":
    m, n, k = map(int, input().split())
    board = [[0]*n for _ in range(m)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for _ in range(k):
        lx, ly, rx, ry = map(int, input().split())
        for y in range(ly, ry):
            for x in range(lx, rx):
                board[y][x] = 1

    res = []
    for j in range(m):
        for i in range(n):
            if board[j][i] == 0:
                res.append(dfs(1, i, j))

    print(len(res))
    print(*sorted(res))