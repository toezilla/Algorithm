import sys
from collections import deque

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.reverse()

    dq = deque()
    for i in range(n):
        if arr[i] == 1:
            dq.appendleft(i + 1)
            continue
        if arr[i] == 2:
            dq.insert(1, i + 1)
            continue
        if arr[i] == 3:
            dq.append(i + 1)
            continue

    print(*dq)
