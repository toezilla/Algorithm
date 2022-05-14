if __name__ == "__main__":
    n = int(input())
    dp = []
    t = []
    for i in range(n):
        t.append(list(map(int, input().split())))
        dp.append([0] * (i + 1))

    dp[0][0] = t[0][0]
    for i in range(1, n):
        for j in range(i + 1):
            if j == 0:
                dp[i][j] = dp[i - 1][j] + t[i][j]
            elif 0 < j < i:
                dp[i][j] = max(dp[i - 1][j - 1] + t[i][j], dp[i - 1][j] + t[i][j])
            elif j == i:
                dp[i][j] = dp[i - 1][j - 1] + t[i][j]
    print(max(dp[n-1]))