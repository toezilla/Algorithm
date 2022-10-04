if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    dp = [0] * (n+1)
    dp[0], maxx = numbers[0], numbers[0]
    for i in range(1, n):
        if numbers[i] > numbers[i]+dp[i-1]:
            dp[i] = numbers[i]
        else:
            dp[i] = numbers[i]+dp[i-1]
        if dp[i] > maxx:
            maxx = dp[i]
    print(maxx)