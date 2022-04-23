import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def dfs(x, y):
    for i in range(4):
        xx = x+dx[i]
        yy = y+dy[i]
        if 0<=xx<=n-1 and 0<=yy<=n-1:
            if visited[yy][xx] == 0:
                if board[yy][xx] == color:
                    visited[yy][xx] = 1
                    dfs(xx, yy)

if __name__ == "__main__":
    n = int(input())
    board = [list(input().rstrip()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]

    cnt1=0
    cnt2=0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for j in range(n):
        for i in range(n):
            if visited[j][i]==0:
                color = board[j][i]
                dfs(i, j)
                cnt1+=1

    for j in range(n):
        for i in range(n):
            if board[j][i] == 'R':
                board[j][i] = 'G'

    visited = [[0]*n for _ in range(n)]

    for j in range(n):
        for i in range(n):
            if visited[j][i]==0:
                color = board[j][i]
                dfs(i, j)
                cnt2+=1


    print(cnt1, cnt2)
