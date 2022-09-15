if __name__ == "__main__":
    n = int(input())
    nums_array = []
    for _ in range(n):
        nums_array.append(int(input()))

    nums_array.sort()
    print(*nums_array)
