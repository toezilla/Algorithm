from collections import deque

n = int(input())
arr = list(map(int, input().split()))

dis = [0]*n
Q = deque()
Q.append(0)

while Q:
    now = Q.popleft()
    if now == n-1:
        break
    else:
        for next in range(now+1, now+arr[now]+1):
            if next<n and dis[next]==0:
                Q.append(next)
                dis[next]=dis[now]+1


if now == (n-1):
    print(dis[now])
else:
    print(-1)