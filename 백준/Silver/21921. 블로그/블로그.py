if __name__ == "__main__":
    n, x = map(int, input().split())
    numbers = list(map(int, input().split()))

    lt = 0
    rt = x-1
    tot = sum(numbers[:rt + 1])
    max_tot = 0
    count = 0

    while rt < n:
        if tot > max_tot:
            max_tot = tot
            count = 1
        elif tot == max_tot:
            count += 1

        if rt == n-1:
            break

        tot -= numbers[lt]
        lt += 1
        rt += 1
        tot += numbers[rt]


    if tot == 0:
        print('SAD')
    else:
        print(max_tot)
        print(count)