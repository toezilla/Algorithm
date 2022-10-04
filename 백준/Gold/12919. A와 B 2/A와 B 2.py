import sys

def operation_1(x: str) -> str:
    return x[:-1]


def operation_2(x: str) -> str:
    return x[::-1][:-1]


def dfs(t: str,  depth: int):
    global count
    if depth == 0:
        if s == t:
            count = 1
        return

    if t[-1] == 'A':
        if t[0] == 'B':
            dfs(operation_2(t), depth-1)
        dfs(operation_1(t), depth-1)

    else:
        if t[0] == 'B':
            dfs(operation_2(t), depth-1)


if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    s = input()
    t = input()
    count = 0
    dfs(t, (len(t) - len(s)))
    print(count)
