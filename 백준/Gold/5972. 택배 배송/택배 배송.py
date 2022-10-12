import heapq

def dijkstra(start, end):
    global min_cost
    q = []
    heapq.heappush(q, (start, 0))
    min_cost[start] = 0

    while q:
        now_node, now_cost = heapq.heappop(q)
        if now_cost > min_cost[now_node]:
            continue

        for x in graph[now_node]:
            next_node, next_cost = x[0], now_cost + x[1]
            if next_cost < min_cost[next_node]:
                min_cost[next_node] = next_cost
                heapq.heappush(q, (next_node, next_cost))

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    min_cost = [2147000000] * (n+1)
    dijkstra(1, n)

    print(min_cost[n])
    