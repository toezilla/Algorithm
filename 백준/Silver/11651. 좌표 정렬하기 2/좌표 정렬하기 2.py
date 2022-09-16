import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    array = []
    for _ in range(n):
        x, y = map(int, input().split())
        array.append((y, x))

    array.sort()
    for item in array:
        print(item[1], item[0])
