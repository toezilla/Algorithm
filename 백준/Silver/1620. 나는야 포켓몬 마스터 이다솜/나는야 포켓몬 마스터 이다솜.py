import sys

if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    pokemon = {}
    for i in range(1, n+1):
        pokemon[i] = (x:=input().rstrip())
        pokemon[x] = i

    for _ in range(m):
        if (x:=input().rstrip())[0].isdigit():
            print(pokemon[int(x)])
        else:
            print(pokemon[x])

