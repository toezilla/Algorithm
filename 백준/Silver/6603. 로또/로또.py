from collections import deque
def DFS(x, cnt, num):
    global res
    if num == 6:
        for i in range(6):
            print(res[i], end=' ')
        print()
        return
    if cnt == k:
        return
    else:
        res[num] = arr[x]
        DFS(x + 1, cnt + 1, num+1)
        DFS(x + 1, cnt + 1, num)


if __name__ == "__main__":
    while True:
        arr = list(map(int, input().split()))
        if arr == [0]:
            break
        arr = deque(arr)
        k = arr.popleft()

        res = [0] * 6
        DFS(0, 0, 0)
        print()