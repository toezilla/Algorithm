from typing import Dict, Tuple, Union
from collections import defaultdict

def make_index(word: str) -> Dict:
    result = defaultdict(list)
    for i in range(len(word)):
        if word.count(word[i]) >= k:
            result[w[i]].append(i)
    return result


def find_string(index: Dict) -> Union[int, Tuple]:
    min_size = 10000
    max_size = 0
    for key in index:
        for i in range(len(index[key])-k + 1):
            size = index[key][i+k-1] - index[key][i] + 1
            if size < min_size:
                min_size = size
            if size > max_size:
                max_size = size

    return min_size, max_size


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w = input()
        k = int(input())

        index = make_index(w)
        if not index:
            print(-1)
        else:
            print(*find_string(index))
