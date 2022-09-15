from typing import List

def rearrange_array(array: List, m: int, n: int) -> List:
    result = []
    for x in range(m):
        for i in range(n):
            if x == 0:
                result.append(array[x][i])
            else:
                result[i] = result[i] + array[x][i]
    return result


if __name__ == "__main__":
    r, c = map(int, input().split())
    words = []
    for _ in range(r):
        words.append(input())
    words = rearrange_array(words,r,  c)

    # BruteForce
    count = 0
    for i in range(1, r):
        check_set = set()
        for word in words:
            if (current := word[i:]) in check_set:
                break
            else:
                check_set.add(current)
        else:
            count += 1

    print(count)
