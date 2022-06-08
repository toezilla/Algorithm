def dfs(start):
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(i)


if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    visited = [False] * (1 + n)
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            if not graph[i]:
                cnt += 1
                visited[i] = True
            else:
                dfs(i)
                cnt += 1
    print(cnt)
    