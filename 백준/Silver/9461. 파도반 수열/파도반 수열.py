if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n in [1,2,3]:
            print(1)
        elif n in [4,5]:
            print(2)
        else:
            dp = [0]*(n+1)
            for i in range(1, 5+1):
                if i<=3:
                    dp[i] = 1
                else:
                    dp[i] = 2
            for i in range(6, n+1):
                dp[i] = dp[i-1]+dp[i-5]
            print(dp[n])
