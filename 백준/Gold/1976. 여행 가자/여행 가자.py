from collections import deque

def bfs(y):
    global target
    visited = [0] * (n)
    q = deque()

    q.append(y)
    visited[y] = 1

    while q:
        cur_y = q.popleft()
        if cur_y == target:
            return True

        for x in range(n):
            if grid[cur_y][x] and not visited[x]:
                q.append(x)
                visited[x] = 1

    return False


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().split())))

    towns = list(map(int, input().split()))
    for i in range(1, m):
        target = towns[i]-1
        if not bfs(towns[i-1]-1):
            print('NO')
            break

    else:
        print('YES')
