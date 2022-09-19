import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m, b = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))

    MAX_SIZE = 257
    answer = 2147000000
    floor = 0
    
    # BruteForce
    for key in range(MAX_SIZE):
        max_key, min_key = 0, 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] >= key:
                    max_key += grid[i][j] - key
                else:
                    min_key += key - grid[i][j]

        if max_key + b >= min_key:
            if min_key + (max_key * 2) <= answer:
                answer = min_key + (max_key * 2)
                floor = key

    print(answer, floor)
    