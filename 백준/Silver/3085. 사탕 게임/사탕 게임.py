def count_row(num: int) -> int:
    result = 0
    cnt = 1
    cur = None
    for i in range(n):
        if grid[num][i] == cur:
            cnt += 1
        else:
            result = max(result, cnt)
            cnt = 1
            cur = grid[num][i]
    result = max(result, cnt)
    return result


def count_col(num: int) -> int:
    result = 0
    cnt = 1
    cur = None
    for i in range(n):
        if grid[i][num] == cur:
            cnt += 1
        else:
            result = max(result, cnt)
            cnt = 1
            cur = grid[i][num]
    result = max(result, cnt)
    return result


if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(input()))

    count = 0
    for i in range(n):
        for j in range(n):
            if 0 <= j+1 < n and grid[i][j] != grid[i][j+1]:
                grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]
                count = max(count, count_row(i), count_col(j), count_col(j+1))
                grid[i][j], grid[i][j+1] = grid[i][j+1], grid[i][j]

            if 0 <= i+1 < n and grid[i][j] != grid[i+1][j]:
                grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]
                count = max(count, count_row(i), count_row(i+1), count_col(j))
                grid[i][j], grid[i+1][j] = grid[i+1][j], grid[i][j]

            count = max(count, count_row(i), count_col(j))

    print(count)
