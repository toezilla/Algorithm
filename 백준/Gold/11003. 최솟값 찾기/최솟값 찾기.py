import sys
import heapq

if __name__ == "__main__":
    input = sys.stdin.readline
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = []
    heap = []

    for i in range(n): # O(n)
        left_bound = (i-l+1)
        right_bound = i

        heapq.heappush(heap, (arr[right_bound], i))

        if left_bound <= 0:
            answer.append(heap[0][0])
            continue

        while heap[0][1] < left_bound:
            heapq.heappop(heap)
        answer.append(heap[0][0])

    print(*answer)