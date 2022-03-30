def dfs(x, y):
    if x < -1 or x > N-1 or y < -1 or y > M-1:
        return False
    
    if visited[x][y] == True:
        return False
    
    visited[x][y] = True
    if graph[x][y] == '-' and (y == M-1 or graph[x][y+1] == '-'):
        dfs(x, y+1)
    elif graph[x][y] == '|' and (x == N-1 or graph[x+1][y] == '|'):
        dfs(x+1, y)
    return True

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

visited = []
for i in range(N):
    temp = []
    for j in range(M):
        temp.append(False)
    visited.append(temp)
    
count = 0
for x in range(N):
    for y in range(M):
        if dfs(x, y) == True:
            count += 1
            
print(count)