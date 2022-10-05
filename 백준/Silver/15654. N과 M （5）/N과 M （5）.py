from itertools import permutations
import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    numbers = list(map(int, input().split()))
    perm = sorted(list(permutations(numbers, m)))

    for item in perm:
        for i in range(m):
            print(item[i], end=' ')
        print()
        