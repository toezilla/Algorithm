import heapq
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        k = int(input())
        max_heap = []
        min_heap = []
        visited = [False] * 1000001

        for i in range(k):
            operation = input().split()
            if operation[0] == 'I':
                value = int(operation[1])
                heapq.heappush(max_heap, (-value, i))
                heapq.heappush(min_heap, (value, i))
                visited[i] = True

            else:
                if operation[1] == '1': # 최댓값 삭제
                    while max_heap and not visited[max_heap[0][1]]:
                        heapq.heappop(max_heap)
                    if max_heap:
                        visited[max_heap[0][1]] = False
                        heapq.heappop(max_heap)
                else:
                    while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                    if min_heap:
                        visited[min_heap[0][1]] = False
                        heapq.heappop(min_heap)

        while min_heap and not visited[min_heap[0][1]]:
            heapq.heappop(min_heap)
        while max_heap and not visited[max_heap[0][1]]:
            heapq.heappop(max_heap)

        if not min_heap or not max_heap:
            print("EMPTY")
        else:
            print(-max_heap[0][0], end = ' ')
            print(min_heap[0][0])