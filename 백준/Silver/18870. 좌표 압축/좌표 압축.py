import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    num_array = list(map(int, input().split()))
    num_set = sorted(list(set(num_array)))
    length = len(num_set)

    answer = []
    dict = {num_set[i]: i for i in range(length)}

    for x in num_array:
        print(dict[x], end = ' ')
