import sys

if __name__ == "__main__":
    input = sys.stdin.readline

    n, m = map(int, input().split())
    answer = 0
    s_dict = {}

    for _ in range(n):
        word = input()
        s_dict[word] = None

    for _ in range(m):
        compare = input()
        if compare in s_dict:
            answer+=1

    print(answer)