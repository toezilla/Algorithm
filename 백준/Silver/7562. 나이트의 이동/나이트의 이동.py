from collections import deque

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        # vars
        n = int(input())
        board = [[-1]*n for _ in range(n)]
        check = [[-1]*n for _ in range(n)]
        start = tuple(map(int, input().split()))
        end = tuple(map(int, input().split()))
        size_x = [min(start[0], end[0]), max(start[0], end[0])]
        size_y = [min(start[1], end[1]), max(start[1], end[1])]

        # collection of possible moves
        dx = [1, 2, 2, 1, -1, -2, -2, -1]
        dy = [2, 1, -1, -2, -2, -1, 1, 2]

        # define queue
        Q = deque()

        # init
        Q.append(start)
        board[start[0]][start[1]] = 0


        # use BFS
        while Q:
            now = Q.popleft()
            if now == end:
                break
            for i in range(8):
                x = now[0]+dx[i]
                y = now[1]+dy[i]

                if 0<=x<=n-1 and 0<=y<=n-1 and check[x][y]<1:
                    if size_x[0]-3<x<size_x[1]+3 and size_y[0]-3<y<size_y[1]+3:
                        Q.append((x, y))
                        board[x][y] = board[now[0]][now[1]]+1
                        check[x][y] = check[now[0]][now[1]]+1

        # generate output
        print(board[now[0]][now[1]])