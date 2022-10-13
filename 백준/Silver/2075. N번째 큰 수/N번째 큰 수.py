import heapq

if __name__ == "__main__":
    n = int(input())
    answer = []
    for _ in range(n):
        inp = list(map(int, input().split()))
        tmp = []
        for x in inp:
            tmp.append(-x)
        tmp += answer
        heapq.heapify(tmp)

        answer = []
        for _ in range(n):
            answer.append(heapq.heappop(tmp))

    answer.sort()
    print(-answer[-1])
    