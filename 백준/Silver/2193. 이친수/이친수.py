if __name__ == "__main__":
    n = int(input())
    dp = [(0, 0) for _ in range(91)]
    dp[1] = (0, 1)
    for i in range(2, n+1):
        dp[i] = (dp[i-1][0]+dp[i-1][1], dp[i-1][0])

    print(dp[n][0]+dp[n][1])