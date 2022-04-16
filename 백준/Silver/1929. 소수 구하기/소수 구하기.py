M, N = map(int, input().split())
ch = [0] * (N+1)
cnt = 0
for i in range(2, N+1):
    if ch[i] == 0:
        if i < M:
            for j in range(i, N+1, i):
                ch[j] = 1
        else:
            for j in range(i, N+1, i):
                ch[j] = 1
            print(i)