def dfs(x, y, n):
    global cnt
    color = grid[y][x]
    for j in range(y, y + n):
        for i in range(x, x + n):
            if color != grid[j][i]:
                dfs(x, y, n // 2)
                dfs(x, y + n // 2, n // 2)
                dfs(x + n // 2, y, n // 2)
                dfs(x + n // 2, y + n // 2, n // 2)
                return
    if color == 0:
        cnt[0] += 1
    else:
        cnt[1] += 1


if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    cnt = [0, 0]
    dfs(0, 0, n)
    print(cnt[0])
    print(cnt[1])
