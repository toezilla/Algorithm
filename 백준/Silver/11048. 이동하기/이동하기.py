if __name__ == "__main__":
    n, m = map(int, input().split())
    maze = []
    for _ in range(n):
        maze.append(list(map(int, input().split())))
    dp = [[0]*(m+1) for _ in range(n+1)]

    for j in range(1, n+1):
        for i in range(1, m+1):
            dp[j][i] = max(dp[j-1][i], dp[j][i-1], dp[j-1][i-1]) + maze[j-1][i-1]

    print(dp[n][m])