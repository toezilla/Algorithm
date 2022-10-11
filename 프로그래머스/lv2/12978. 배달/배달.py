import heapq

def dijkstra(start, end, n, graph):
    min_cost = [2147000000] * (n+1)
    q = []
    heapq.heappush(q, (start, 0))
    min_cost[start] = 0

    while q:
        cur_node, cur_cost = heapq.heappop(q)
        if min_cost[cur_node] < cur_cost:
            continue
        
        for x in graph[cur_node]:
            next_node, next_cost = x[0], cur_cost + x[1]
            
            if next_cost < min_cost[next_node]:
                min_cost[next_node] = next_cost
                heapq.heappush(q, (next_node, next_cost))
    
    print(min_cost)
    return min_cost[end]


def solution(N, road, K):
    answer = 1
    graph = [[] for _ in range((N+1))]
    for x in road:
        graph[x[0]].append((x[1], x[2]))
        graph[x[1]].append((x[0], x[2]))
    
    for i in range(2, N+1):
        if dijkstra(1, i, N, graph) <= K:
            answer += 1

    return answer
