import sys
from itertools import combinations
import math

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input().rstrip())
    for i in range(n):
        m = int(input())
        x_total, y_total = 0, 0
        coords = []
        for i in range(m):
            x, y = map(int, input().split())
            x_total += x
            y_total += y
            coords.append([x, y])

            comb = list(combinations(coords, m//2))
            comb_half_len = len(comb) // 2
            answer = float('inf')
            for part in comb[:comb_half_len]:

                x1_total, y1_total = 0, 0
                for x1, y1 in part:
                    x1_total += x1
                    y1_total += y1

                x2_total = x_total - x1_total
                y2_total = y_total - y1_total

                answer = min(answer, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))

        print('{:.12f}'.format(answer))
        