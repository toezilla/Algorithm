if __name__ == "__main__":
    n = int(input())
    cards = list(map(int, input().split()))
    dp = [0] * (1001)

    dp[1] = cards[0]
    for i in range(2, n+1):
        tmp = -1
        for j in range(i):
            if (num:=dp[j]+cards[i-j-1])>tmp:
                tmp = num
        dp[i] = tmp
    print(dp[n])