from collections import deque

if __name__ == "__main__":
    n, m = map(int, input().split())
    maze  = [[0]*m for _ in range(n)]
    dist = [[0]*m for _ in range(n)]

    for i in range(n):
        string = input()
        for j in range(m):
            maze[i][j] = int(string[j])

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    Queue = deque()
    Queue.append((0,0))
    maze[0][0]=1

    while Queue:
        now = Queue.popleft()
        for i in range(4):
            x = now[0]+dx[i]
            y = now[1]+dy[i]
            if 0<=x<n and 0<=y<m and maze[x][y]==1:
                maze[x][y] = 0
                dist[x][y] = dist[now[0]][now[1]]+1
                Queue.append((x,y))

    print(dist[n-1][m-1]+1)