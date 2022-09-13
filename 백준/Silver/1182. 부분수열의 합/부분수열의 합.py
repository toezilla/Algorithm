from itertools import combinations

if __name__ == "__main__":
    n, s = map(int, input().split())
    sequence = list(map(int, input().split()))

    count = 0
    for i in range(1, n+1):
        for val in combinations(sequence, i):
            if sum(val) == s:
                count+=1

    print(count)
    