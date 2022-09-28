def get_slope(from_, to_, array):
    answer = (array[from_] - array[to_]) / (from_ - to_)
    return answer

if __name__ == "__main__":
    n = int(input())
    buildings = list(map(int, input().split()))
    answer = -1

    for i in range(n):
        left_min = float(2147000000)
        right_max = float(-2147000000)
        count = 0
        for j in range(i-1, -1, -1):
            if (cur_slope := get_slope(i, j, buildings)) < left_min:
                left_min = cur_slope
                count += 1
        for j in range(i+1, n):
            if (cur_slope := get_slope(i, j, buildings)) > right_max:
                right_max = cur_slope
                count += 1
        answer = max(answer, count)
    print(answer)
    