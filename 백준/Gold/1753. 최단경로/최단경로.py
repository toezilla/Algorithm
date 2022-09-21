import sys
import heapq

def dijkstra(start):
    global distance
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for x in graph[now]:
            cost = dist + x[1]
            if cost < distance[x[0]]:
                distance[x[0]] = cost
                heapq.heappush(queue, (cost, x[0]))

if __name__ == "__main__":
    INF = 2147000000
    input = sys.stdin.readline

    v, e = map(int, input().split())
    k = int(input())

    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    distance = [INF] * (v+1)
    dijkstra(k)
    distance = distance[1:]
    for x in distance:
        if x == 2147000000:
            print('INF')
            continue
        print(x)