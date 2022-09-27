import heapq

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    cost[0][0] = graph[0][0]

    while q:
        cur_cost, cur_x, cur_y = heapq.heappop(q)

        if cur_x == n-1 and cur_y == n-1:
            return cost[cur_x][cur_y]

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0<=next_x<n and 0<=next_y<n:
                next_cost = cur_cost + graph[next_x][next_y]

                if next_cost < cost[next_x][next_y]:
                    cost[next_x][next_y] = next_cost
                    heapq.heappush(q, (next_cost, next_x, next_y))


if __name__ == "__main__":
    INF = 2147000000
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    num = 1
    
    while True:
        n = int(input())
        if n == 0:
            break

        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))
            cost = [[INF] * n for _ in range(n)]

        result = dijkstra()
        print(f"Problem {num}: {result}")
        num+=1
        