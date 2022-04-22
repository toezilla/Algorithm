def dfs(x, y):
    global answer
    global maze
    global cnt

    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0<=next_x<=n-1 and 0<=next_y<=n-1:
            if maze[next_x][next_y] == 1:
                maze[next_x][next_y] = 0
                dfs(next_x, next_y)
                cnt += 1


if __name__ == "__main__":
    n = int(input())
    maze = []
    village_number = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(n):
        tmp = []
        for s in input():
            tmp.append(int(s))
        maze.append(tmp)

    res = []
    for i in range(n):
        for j in range(n):
            if maze[i][j] == 1:
                cnt = 1
                maze[i][j] = 2
                dfs(i, j)
                res.append(cnt)

    res.sort()
    print(len(res))
    for i in res:
        print(i)