def dfs(start):
    global cnt
    visited[start] = 1
    for i in graph[start]:
        if visited[i]==0:
            dfs(i)
            cnt+=1
if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph = [[]*n for _ in range(n+1)]
    for _ in range(m):
        from_, to_ = map(int, input().split())
        graph[from_].append(to_)
        graph[to_].append(from_)

    visited = [0]*(n+1)
    cnt = 0
    dfs(1)
    print(cnt)