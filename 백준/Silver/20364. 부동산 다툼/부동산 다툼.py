import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
ducks = [int(input())for _ in range(Q)]

visited = set()

for i in range(Q):
    result = 0
    duck = ducks[i]
    while duck > 1:
        if duck in visited:
            result = duck
        duck //= 2
    visited.add(ducks[i])

    print(result)