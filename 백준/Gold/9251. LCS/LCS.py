import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    words_a = input()
    words_b = input()

    dp = [[0] * (len(words_b)+1) for _ in range(len(words_a)+1)]

    for i in range(1, len(words_a)):
        for j in range(1, len(words_b)):
            if words_a[i-1] == words_b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                continue
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    print(dp[len(words_a)-1][len(words_b)-1])
    