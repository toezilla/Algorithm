import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    answer = []

    for _ in range(n):
        name, k, e, m = map(str, input().split())
        answer.append((int(k), int(e), int(m), name))

    answer.sort(key = lambda x: (-x[0], x[1], -x[2], x[3]))
    for item in answer:
        print(item[3])

