import sys

def dfs(x):
    global check
    if not check[array[x]-1]:
        check[array[x]-1] = 1
        dfs(array[x]-1)


if __name__ == "__main__":
    sys.setrecursionlimit(10**5)
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int, input().split()))
        check = [0] * (size:=len(array))
        count = 0
        for i in range(size):
            if not check[i]:
                dfs(i)
                count +=1
        print(count)