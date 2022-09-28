if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    count = 0

    for i in range(n):
        tmp = arr[:i] + arr[i+1:]
        lt, rt = 0, len(tmp)-1
        while lt < rt:
            key = tmp[lt] + tmp[rt]
            if key == arr[i]:
                count += 1
                break
            if key < arr[i]:
                lt += 1
            else:
                rt -= 1
    print(count)
    