from itertools import combinations

if __name__ == "__main__":
    n, k = map(int, input().split())
    if k < 5:
        print(0)
        exit()

    k -= 5
    a_set = {'a', 'n', 't', 'i', 'c'}
    a_list = []

    alphabets = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z') + 1))) - a_set))}

    max_count = 0
    for _ in range(n):
        tmp = 0
        for c in set(input()) - a_set:
            tmp |= (1 << alphabets[c])
        a_list.append(tmp)

    power_by_2 = (2 ** i for i in range(21))

    for combi in combinations(power_by_2, k):
        combi_sum = sum(combi)

        count = 0
        for bit in a_list:
            if combi_sum & bit == bit:
                count += 1

        max_count = max(max_count, count)
    print(max_count)
    