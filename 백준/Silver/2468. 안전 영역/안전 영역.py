import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global visited
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<n and 0<=yy<n:
            if safe_area[yy][xx] == 1 and visited[yy][xx] == 0:
                visited[yy][xx] = 1
                dfs(xx, yy)

if __name__ == "__main__":
    n = int(input())
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    area = []
    maxx = 0
    minn = 2147000000
    for _ in range(n):
        tmp = list(map(int, input().split()))
        area.append(tmp)
        maxx_tmp = max(tmp)
        minn_tmp = min(tmp)
        if maxx_tmp > maxx:
            maxx = maxx_tmp
        if minn_tmp < minn:
            minn = minn_tmp

    res = 0
    for x in range(minn-1, maxx):
        cnt = 0
        safe_area = [[0] * n for _ in range(n)]
        visited = [[0]*n for _ in range(n)]
        for j in range(n):
            for i in range(n):
                if area[j][i]>x:
                    safe_area[j][i] = 1
        for j in range(n):
            for i in range(n):
                if safe_area[j][i] == 1 and visited[j][i] == 0:
                    visited[j][i] = 1
                    dfs(i, j)
                    cnt+=1
        if cnt > res:
            res = cnt
    print(res)