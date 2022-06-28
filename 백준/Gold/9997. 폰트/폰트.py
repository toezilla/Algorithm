from sys import stdin

def dfs(count, mask):
    global result
    if count == n - 1:
        if mask == alphabet:
            result += 1
    else:
        dfs(count + 1, mask | words[count + 1])
        dfs(count + 1, mask)


if __name__ == "__main__":
    alphabet = (1 << 26) - 1
    result = 0

    n = int(stdin.readline())
    words = [0 for _ in range(n)]
    for i in range(n):
        word = stdin.readline().strip()
        for w in word:
            words[i] |= 1 << ord(w) - 97

    dfs(-1, 0)

    print(result)
    