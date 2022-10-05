import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    memo = set()

    for _ in range(n):
        memo.add(input()[:-1])

    for _ in range(m):
        tmp = list(input().split(','))
        tmp[-1] = tmp[-1][:-1]

        for word in tmp:
            if word in memo:
                memo.remove(word)
        print(len(memo))
        