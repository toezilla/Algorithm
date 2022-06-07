import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m, k = map(int, input().split())
    dp = [[1]*(m+1) for _ in range(n+1)]
    
    for j in range(1, n+1):
        for i in range(1, m+1):
            dp[j][i] = dp[j-1][i] + dp[j][i-1]
    
    if dp[n][m] < k:
        print(-1)
    else:
        res = ""
        while True:
            if n==0 or m==0:
                res+="z"*m
                res+="a"*n
                break
            
            tmp = dp[n-1][m]
            if k <= tmp:
                res+="a"
                n-=1
            else:
                res+="z"
                m-=1
                k-=tmp
        print(res)
        