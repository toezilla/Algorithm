if __name__ == "__main__":
    n, s = map(int, input().split())
    array = list(map(int, input().split()))
    answer = 100001
    cur_sum = array[0]
    lt, rt = 0, 0

    while True:
        if cur_sum >= s:
            cur_sum -= array[lt]
            answer = min(rt-lt+1, answer)
            lt += 1
            continue

        rt += 1
        if rt == n:
            break

        cur_sum += array[rt]

    if answer == 100001:
        print(0)
    else:
        print(answer)
