import sys
sys.setrecursionlimit(10**6)

def dfs(x, y):
    global visited
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if 0<=next_x<w and 0<=next_y<h and visited[next_y][next_x] == 0:
            if graph[next_y][next_x] == '#':
                visited[next_y][next_x] = 1
                dfs(next_x, next_y)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        graph = []
        for _ in range(h):
            graph.append(list(input()))
        visited = [[0] * w for _ in range(h)]

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        cnt = 0
        for j in range(h):
            for i in range(w):
                if visited[j][i] == 0 and graph[j][i] == '#':
                    visited[j][i] = 1
                    dfs(i, j)
                    cnt+=1

        print(cnt)