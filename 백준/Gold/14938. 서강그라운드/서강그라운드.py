import sys
import heapq

def dijkstra(start):
    global costs
    queue = []
    heapq.heappush(queue, (start, 0))
    costs[start] = 0

    while queue:
        now_node, now_cost = heapq.heappop(queue)

        for edge in edges[now_node]:
            next_node = edge[0]
            next_cost = now_cost + edge[1]

            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                heapq.heappush(queue, (next_node, next_cost))


if __name__ == "__main__":
    input = sys.stdin.readline

    n, m, r = map(int, input().split())

    nodes = [0] + list(map(int, input().split()))
    edges = [[] for _ in range(n+1)]
    for _ in range(r):
        start, end, cost = map(int, input().split())
        edges[start].append((end, cost))
        edges[end].append((start, cost))

    max_total = 0
    for i in range(1, n+1):
        total = 0
        costs = [2147000000] * (n+1)
        dijkstra(i)
        for j in range(1, n+1):
            if costs[j] <= m:
                total += nodes[j]
        max_total = max(total, max_total)

    print(max_total)
    