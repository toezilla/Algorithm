from collections import defaultdict

if __name__ == "__main__":
    dp = [-1] * 10001
    shortcut = defaultdict(list)

    n, d = map(int, input().split())
    for _ in range(n):
        s, e, l = map(int, input().split())
        shortcut[e].append((s, l))

    dp[0] = 0
    for i in range(1, d+1):
        dp[i] = dp[i-1] + 1
        if i in shortcut:
            for value in shortcut[i]:

                if (val := value[1] + dp[value[0]]) < dp[i]:
                    dp[i] = val
    print(dp[d])
