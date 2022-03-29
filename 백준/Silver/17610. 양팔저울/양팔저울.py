def DFS(L, Sum):
    global res
    if L==n:
        if 0<Sum<=s:
            res.add(Sum)
    else:
        DFS(L+1, Sum+G[L])
        DFS(L+1, Sum-G[L])
        DFS(L+1, Sum)

if __name__ == "__main__":
    n = int(input())
    G = list(map(int, input().split()))
    s = sum(G)
    res = set()
    DFS(0, 0)
    print(s-len(res))