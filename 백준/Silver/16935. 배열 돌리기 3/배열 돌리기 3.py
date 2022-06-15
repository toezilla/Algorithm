if __name__ == "__main__":
    n, m, r = map(int, input().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    functions = list(map(int, input().split()))



    for f in functions:

        if f == 1:
            for i in range(n // 2):
                grid[i], grid[-i - 1] = grid[-i - 1], grid[i]
        elif f == 2:
            for i in range(n):
                for j in range(m // 2):
                    grid[i][j], grid[i][-j - 1] = grid[i][-j - 1], grid[i][j]
        elif f == 3:
            grid_new = []
            for i in range(m):
                tmp = []
                for j in range(n-1, -1, -1):
                    tmp.append(grid[j][i])
                grid_new.append(tmp)
            n, m = m, n
            grid = grid_new[:][:]

        elif f == 4:
            grid_new = []
            for i in range(m-1, -1, -1):
                tmp = []
                for j in range(n):
                    tmp.append(grid[j][i])
                grid_new.append(tmp)
            n, m = m, n
            grid = grid_new[:][:]

        elif f == 5:
            grid_new = [[-1]*m for _ in range(n)]
            for i in range(n//2):
                for j in range(m//2):
                    grid_new[i][j+m//2] = grid[i][j]
            for i in range(n//2, n):
                for j in range(m//2):
                    grid_new[i-n//2][j] = grid[i][j]
            for i in range(n//2):
                for j in range(m//2, m):
                    grid_new[i+n//2][j] = grid[i][j]
            for i in range(n//2, n):
                for j in range(m//2, m):
                    grid_new[i][j-m//2] = grid[i][j]
            grid = grid_new[:][:]

        elif f == 6:
            grid_new = [[-1] * m for _ in range(n)]
            for i in range(n // 2):
                for j in range(m // 2):
                    grid_new[i+n//2][j] = grid[i][j]
            for i in range(n // 2, n):
                for j in range(m // 2):
                    grid_new[i][j+m//2] = grid[i][j]
            for i in range(n // 2):
                for j in range(m // 2, m):
                    grid_new[i][j-m//2] = grid[i][j]
            for i in range(n // 2, n):
                for j in range(m // 2, m):
                    grid_new[i-n//2][j] = grid[i][j]
            grid = grid_new[:][:]

    for x in grid:
        for s in x:
            print(s, end = ' ')
        print()