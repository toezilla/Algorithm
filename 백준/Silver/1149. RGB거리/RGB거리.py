if __name__ == "__main__":
    n = int(input())
    dp = []
    for _ in range(n):
        dp.append(list(map(int, input().split())))
    for i in range(1, n):
        # i번째 집을 빨강으로 칠할 때
        dp[i][0] = min(dp[i-1][1], dp[i-1][2])+dp[i][0]

        # i번째 집을 초록으로 칠할 때
        dp[i][1] = min(dp[i-1][0], dp[i-1][2])+dp[i][1]

        # i번째 집을 파랑으로 칠할 때
        dp[i][2] = min(dp[i-1][0], dp[i-1][1])+dp[i][2]

	# 최솟값 출력
    print(min(dp[n-1]))