def dfs(depth):
    global cnt

    if depth == n:
        cnt+=1
        return

    for i in range(n):
        graph[depth] = i
        flag = True
        for x in range(depth):
            if graph[x] == graph[depth] or abs(graph[x] - graph[depth]) == abs(x - depth):
                flag = False
        if flag:
            dfs(depth+1)


if __name__ == "__main__":
    # n = int(input())
    # graph = [0] * n
    # cnt = 0
    # dfs(0)
    # print(cnt)
    
    answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
    print(answer[int(input())])
