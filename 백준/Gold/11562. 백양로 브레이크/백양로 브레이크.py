import sys

if __name__ == "__main__":
    INF = sys.maxsize
    
    input = sys.stdin.readline
    n, m = map(int, input().rstrip().split())
    nodes = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        nodes[i][i] = 0
    for _ in range(m):
        u, v, b = map(int, sys.stdin.readline().rstrip().split())
        if b == 0:
            nodes[u][v] = 0
            nodes[v][u] = 1
        
        else:
            nodes[u][v] = 0
            nodes[v][u] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if nodes[i][j] > nodes[i][k] + nodes[k][j]:
                    nodes[i][j] = nodes[i][k] + nodes[k][j]

    k = int(sys.stdin.readline().rstrip())

    for _ in range(k):
        s, e = map(int, sys.stdin.readline().rstrip().split())
        print(nodes[s][e])
