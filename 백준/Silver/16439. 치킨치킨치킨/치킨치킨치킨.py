from itertools import combinations

if __name__ == '__main__':
    n, m = map(int, input().split())
    chickens = [i for i in range(m)]
    orders = list(combinations(chickens, 3))

    satisfies = []
    for _ in range(n):
        satisfies.append(list(map(int, input().split())))

    max_score = 0
    for order in orders:
        score = 0
        for satisfy in satisfies:
            score += max(satisfy[order[0]], satisfy[order[1]], satisfy[order[2]])

        max_score = max(max_score, score)

    print(max_score)
    