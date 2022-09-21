import sys
import heapq
from typing import List

def dijkstra(start: int, distance: List) -> List:
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0

    while q:
        cur_node, cur_cost = heapq.heappop(q)
        if distance[cur_node] < cur_cost:
            continue
            
        for val in graph[cur_node]:
            next_node = val[0]
            next_cost = cur_cost + val[1]
            if next_cost < distance[next_node]:
                distance[next_node] = next_cost
                heapq.heappush(q, (next_node, next_cost))
    return distance


if __name__ == "__main__":
    INF = 2147000000
    input = sys.stdin.readline

    v, e, x = map(int, input().split())
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        s, e, c = map(int, input().split())
        graph[s].append((e, c))

    max_time = [-1] * (v+1)
    for i in range(1, v+1):
        distance_1 = [INF] * (v + 1)
        distance_2 = [INF] * (v+1)

        distance_1 = dijkstra(i, distance_1)
        distance_2 = dijkstra(x, distance_2)
        max_time[i] = distance_1[x] + distance_2[i]

    print(max(max_time))
    