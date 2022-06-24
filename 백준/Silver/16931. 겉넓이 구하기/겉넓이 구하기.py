if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    up = n*m
    
    side = 0
    for i in range(n):
        for j in range(m):
            if j == 0:
                side += grid[i][j]
            else:
                if grid[i][j-1] < grid[i][j]:
                    side += grid[i][j] - grid[i][j-1]
    
    front = 0
    for j in range(m):
        for i in range(n):
            if i == 0:
                front += grid[i][j]
            else:
                if grid[i-1][j] < grid[i][j]:
                    front += grid[i][j] - grid[i-1][j]
    
    answer = 2*(up+side+front)
    print(answer)
    