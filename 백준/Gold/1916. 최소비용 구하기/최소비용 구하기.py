import heapq
import sys

def dijkstra(start: int) -> None:
    global min_cost

    q = []
    heapq.heappush(q, (start, 0))
    min_cost[start] = 0

    while q:
        now_node, now_cost = heapq.heappop(q)
        if min_cost[now_node] < now_cost:
            continue

        for x in graph[now_node]:
            next_node = x[0]
            next_cost = now_cost + x[1]
            if next_cost < min_cost[next_node]:
                min_cost[next_node] = next_cost
                heapq.heappush(q, (next_node, next_cost))


if __name__ == "__main__":
    input = sys.stdin.readline
    INF = 2147000000

    n = int(input())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    min_cost = [INF] * 1001

    for _ in range(m):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))

    start, end = map(int, input().split())
    dijkstra(start)
    print(min_cost[end])
    