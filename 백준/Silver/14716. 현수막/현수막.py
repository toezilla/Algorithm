import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    global visited
    for i in range(8):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<m:
            if visited[yy][xx] == 0 and banner[yy][xx] == 1:
                visited[yy][xx] = 1
                dfs(xx, yy)

if __name__ == "__main__":
    m, n = map(int, input().split())
    dx = [1, -1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, 1, -1, 1, -1, 1, -1]
    cnt = 0
    visited = [[0]*(n+1) for _ in range(m+1)]
    banner = []
    for _ in range(m):
        banner.append(list(map(int, input().split())))

    for j in range(m):
        for i in range(n):
            if visited[j][i]==0 and banner[j][i]==1:
                cnt+=1
                dfs(i, j)
    print(cnt)