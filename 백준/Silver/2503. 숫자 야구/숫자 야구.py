import sys
from itertools import permutations

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    cases = []

    for _ in range(n):
        num, s, b = map(int, input().split())
        cases.append((str(num), s, b))

    possibles = list(permutations(list(x for x in range(1, 10)), 3))

    count = 0
    for possible in possibles:
        for case in cases:
            strikes, balls = 0, 0
            for i in range(3):
                if str(possible[i]) in case[0]:
                    if possible[i] == int(case[0][i]):
                        strikes += 1
                    else:
                        balls += 1
            if strikes != case[1] or balls != case[2]:
                break
        else:
            count+=1

    print(count)
