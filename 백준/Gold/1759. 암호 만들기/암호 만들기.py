from itertools import combinations


if __name__ == "__main__":
    l, c = map(int, input().split())
    con_set = {'a', 'e', 'i', 'o', 'u'}
    answer = []

    words_list = list(input().split())
    combi_list = list(combinations(words_list, l))

    for items in combi_list:
        items_list = list(items)
        con_cnt = 0
        for item in items_list:
            if item in con_set:
                con_cnt += 1
        if con_cnt >= 1 and l - con_cnt >= 2:
            tmp = ''
            for item in sorted(items_list):
                tmp = tmp + item
            answer.append(tmp)

    for x in sorted(answer):
        print(x)
