if __name__ == "__main__":
    max_row, max_col = map(int,input().split())

    row_array = [0, max_row]
    col_array = [0, max_col]

    n = int(input())
    for _ in range(n):
        row, cut = map(int, input().split())
        if row:
            row_array.append(cut)
        else:
            col_array.append(cut)

    row_array.sort()
    col_array.sort()

    max_subtracted = [-1, -1]

    for i in range(len(row_array)-1):
        if (row_tmp := row_array[i+1] - row_array[i]) > max_subtracted[0]:
            max_subtracted[0] = row_tmp
    for i in range(len(col_array)-1):
        if (col_tmp := col_array[i+1] - col_array[i]) > max_subtracted[1]:
            max_subtracted[1] = col_tmp

    print(max_subtracted[0] * max_subtracted[1])
