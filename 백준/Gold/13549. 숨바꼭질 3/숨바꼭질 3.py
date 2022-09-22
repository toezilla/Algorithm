from collections import deque

def bfs(x: int):
    q = deque()
    q.append(x)
    arr[x] = 0

    while q:
        s = q.popleft()

        if s == k:
            return arr[s]

        if 0 <= s - 1 < LIMIT and arr[s - 1] == -1:
            arr[s - 1] = arr[s] + 1
            q.append(s - 1)

        if 0 < s * 2 < LIMIT and arr[s * 2] == -1:
            arr[s * 2] = arr[s]
            q.appendleft(s * 2)

        if 0 <= s + 1 < LIMIT and arr[s + 1] == -1:
            arr[s + 1] = arr[s] + 1
            q.append(s + 1)


if __name__ == "__main__":
    LIMIT = 100001

    n, k = map(int, input().split())
    arr = [-1] * LIMIT
    print(bfs(n))