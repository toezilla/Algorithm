import sys
from typing import List


def search(array: List) -> int:
    default = -1
    for i in range(len(array)-2):
        if array[i] < array[i+1] + array[i+2]:
            return array[i] + array[i+1] + array[i+2]
    return default


if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    array = []
    for _ in range(n):
        array.append(int(input()))

    array.sort(reverse = True)
    print(search(array))
