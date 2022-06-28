import heapq

if __name__ == "__main__":
    n = int(input())
    dasom = int(input())

    heap = []
    for _ in range(n - 1):
        num = int(input())
        heapq.heappush(heap, (-num, num))


    if len(heap) == 0:
        print(0)

    else:
        count = 0
        while True:
            now = heapq.heappop(heap)[1]
            if now >= dasom:
                count += 1
                dasom += 1
                heapq.heappush(heap, (-now + 1, now - 1))
            else:
                break

        print(count)