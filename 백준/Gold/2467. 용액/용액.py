if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))

    _min = 2147000000
    min_val = []
    lt, rt = 0, n-1
    while lt < rt:
        if abs(array[lt] + array[rt]) < _min:
            _min = abs(array[lt]+array[rt])
            min_val = [array[lt], array[rt]]

        if array[lt]+array[rt] < 0:
            lt += 1
        elif array[lt]+array[rt] > 0:
            rt -= 1
        else:
            break

    print(*min_val)
    