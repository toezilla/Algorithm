def DFS(x, num):
    global min
    if num > min:
        return
    if x == 1:
        if num < min:
            min = num
    else:
        if x % 3 == 0:
            DFS(x // 3, num + 1)
        DFS(x - 1, num + 1)
        if x%2 == 0:
            DFS(x // 2, num + 1)


if __name__ == "__main__":
    n = int(input())
    min = 2147000000
    DFS(n, 0)

    print(min)