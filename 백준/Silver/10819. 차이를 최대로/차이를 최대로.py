from itertools import permutations

def operation(array):
    result = 0
    for i in range(len(array)-1):
        result += abs(array[i+1]-array[i])
    return result


if __name__ == "__main__":
    n = int(input())
    array = list(map(int, input().split()))
    perm = list(permutations(array, n))

    answer = -2147000000
    for i in range(len(perm)):
        arr = list(perm[i])
        if (tmp := operation(arr)) > answer:
            answer = tmp
    print(answer)
